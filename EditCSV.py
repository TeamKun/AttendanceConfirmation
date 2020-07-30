import pandas as pd
import glob

#複数ファイル読み込み準備
allFiles = glob.glob("Source/*.csv")
frame = pd.DataFrame()

#ファイルを一つずつ読み込む
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None,header=0,encoding="utf-8")
    
    #Discord ID でユニーク化
    df = df.drop_duplicates(["Discord ID"])
    #list_.append(df[["Discord ID","Discord 名前"]])
    list_.append(df[["Discord ID"]])
df = pd.concat(list_)

#DiscordのIDを隠す。
#def hidetag(x):
#    return x.rpartition("#")[0]
#df["Discord 名前"] = df["Discord 名前"].map(hidetag)

#結果を書き出し
df.to_csv("Output/output.csv",index=False,header=False)