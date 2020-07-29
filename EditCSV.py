import pandas as pd
import glob
import math

#複数ファイル読み込み。1つのデータフレームに。
allFiles = glob.glob("Source/*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None,header=0,encoding="utf-8")
    #Discord ID でユニーク化
    df = df.drop_duplicates(["Discord ID"])
    list_.append(df)
df = pd.concat(list_)
df = df["Discord ID"].value_counts()
df.to_csv("Output/output.csv")