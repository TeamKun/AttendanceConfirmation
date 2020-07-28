import csv

CountDic = {}
#入退室判定に利用する人のDiscordID
SessionHostId = "213535369881190401"
#CSV展開
with open(r"C:\Users\20170511\Desktop\Graph from CSV\Graph from CSV\2020-07-29.csv",encoding='utf8') as f:
    reader = csv.reader(f)
    #ヘッダーをスキップ
    skip = next(reader)
    #readerをリストに格納
    l = [row for row in reader]

    for i in range(len(l)):
        member = l[i][3]
        CountDic.setdefault(member, 0)
        CountDic[member] += 1
        #if l[i + 1][2] == SessionHostId:
            #break
for key, value in CountDic.items():
    print('{}: {}'.format(key, value))