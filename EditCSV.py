import pandas as pd
import glob
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from apiclient import discovery

#複数ファイル読み込み準備
allFiles = glob.glob("Source/*.csv")
frame = pd.DataFrame()

#ファイルを一つずつ読み込む
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None,header=0,encoding="utf-8")
    
    #Discord ID でユニーク化
    df = df.drop_duplicates(["Discord ID"])
    list_.append(df[["Discord ID"]])
df = pd.concat(list_)

#結果を書き出し
df.to_csv("Output/output.csv",index=False,header=False)

#Googleスプレッドシート認証
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('alpine-task-283616-88ce89d7568d.json', scope)

#GoogleAPIにログイン
gc = gspread.authorize(credentials)

#データフレームを文字列型に変換
df = df[["Discord ID"]].astype(str)

#データを入れるスプレッドシートと範囲を指定
spreadsheet_id = ""
sheet_name = "データ"
sheet_range = "A2"
_range = f"{sheet_name}!{sheet_range}"

#データを入れる
dat = df.values.tolist()
body = {"values": dat}
value_input_option = "USER_ENTERED"
service = discovery.build('sheets', 'v4', credentials= credentials)
request = service.spreadsheets().values().update(spreadsheetId=spreadsheet_id,valueInputOption=value_input_option,range=_range,body=body)
request.execute()