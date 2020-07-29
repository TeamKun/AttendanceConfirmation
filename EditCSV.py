import pandas as pd
import glob

#複数ファイル読み込み。1つのデータフレームに。
allFiles = glob.glob("*.csv")
frame = pd.DataFrame()
list_ = []
for file_ in allFiles:
    df = pd.read_csv(file_,index_col=None,header=0,encoding="utf-8")
    list_.append(df)
df = pd.concat(list_)