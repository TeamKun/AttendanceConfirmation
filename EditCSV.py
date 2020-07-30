import pandas as pd
import glob
import gspread
import json
from oauth2client.service_account import ServiceAccountCredentials 

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

#スプレッドシートキー
SPREADSHEET_KEY = "1b81qXNJ2R1KxEcMx-n77blXHzGrDM6CkLu_7eWX-Znw"

#共有設定したスプレッドシートのデータを開く
wks = gc.open_by_key(SPREADSHEET_KEY).worksheet("データ")

#編集する範囲を指定
cell_list = wks.range('A1:A'+str(len(df)))

#スプレッドシートにデータを流し込む
for i,cell in enumerate(cell_list):
    cell.value = df[["Discord ID"]]

#最終反映
wks.update_cells(wks.range('A1:A'+str(len(df))))