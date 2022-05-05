"""
ID: xie_jj2
LANG: PYTHON3
TASK: gift1
"""

fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')
np = int(fin.readline())
giftDict={}

for i in range (np):
    name = fin.readline().rstrip('\n')
    giftDict[name]=0

for i in range (np):
    name = fin.readline().rstrip('\n')
    (amt, num) = map (int, fin.readline().split())
    if(num > 0):
        gift = int(amt/num)
        reminder = amt%num
    else:
        gift = 0
        reminder = 0
    giftDict[name] += reminder - amt
    for j in range(num):
        name = fin.readline().rstrip('\n')
        giftDict[name] += gift

for name in giftDict:
    print(name, giftDict[name])
    fout.write(name+" "+ str(giftDict[name])+"\n")

fout.close()
