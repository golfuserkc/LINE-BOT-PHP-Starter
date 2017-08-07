#!/usr/bin/python
#-*-coding: utf-8 -*-
import PyICU
import pymysql
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='projectone',charset = "utf8mb4")
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=None, db='mysql')
def warp_split(str):
    str.replace(" ", "")
    tmp = warp(str).split("|")
    return tmp

def isThai(chr):
    cVal = ord(chr)
    if (cVal >= 3584 and cVal <= 3711):
        return True
    return False


def warp(txt):
    # print(txt)
    bd = PyICU.BreakIterator.createWordInstance(PyICU.Locale("th"))
    bd.setText(txt)
    lastPos = bd.first()
    retTxt = ""
    try:
        while (1):
            currentPos = next(bd)
            retTxt += txt[lastPos:currentPos]
            # เฉพาะภาษาไทยเท่านั้น
            if (isThai(txt[currentPos - 1])):
                if (currentPos < len(txt)):
                    if (isThai(txt[currentPos])):
                        # คั่นคำที่แบ่ง
                        retTxt += "|"
            lastPos = currentPos
    except StopIteration:
        pass
        # retTxt = retTxt[:-1]
    return retTxt

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='projectone',charset = "utf8mb4")
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=None, db='mysql')

cursor = conn.cursor()
query = ("Select company_name From ocpb")
cursor.execute(query)
data = cursor.fetchall()

kebkum = list(data)
kebkum2 = []


for c in data:
    word = str(c)
    word =word.replace("('","")
    word = word.replace("',)","")
    word = word.replace(" ","")
    kebkum2.append(warp(word))

arraylist_kebkum = []

cutkum = {}
cutkum["num"] = 0
# cutkum["company"]
for c in range(len(kebkum2)):
    cutkum[c] = kebkum2[c].split("|")
    #arraylist_kebkum.append(c.split("|"))
#for i in cutkum:
    #print(i)
#for c in arraylist_kebkum:
    #print(c)

word = 'บริษัทกานดาเคหะจำกัด'
ww = warp_split(word)
word = word.replace(" ", "")
#print(word)

kebkum02 = []
kebkum02.append(warp(word))
#print(kebkum2)

arraylist_kebkum = []
arraylist_kebkum.append(kebkum2[0].split("|"))

arraylist_inkebkum = []
# print(kebkum2[0])

id = {}
for i,n in enumerate(kebkum2):
    arraylist_inkebkum.append(n.split("|"))
    id[i] = n



arraylist_kebcount = []

for i in range(len(data)):
    nubkummean = 0
    for c in arraylist_inkebkum[i]:
        for n in arraylist_kebkum[0]:
            if(n==c):
                nubkummean+=1
    id[i] = [id[i],nubkummean]
    print(id[i])

"""
#for c in arraylist_inkebkum:
print("kkkk",arraylist_inkebkum[0])
sum = []

for data in arraylist_inkebkum:
    s_ = 0
    for i in ww:
        co = data.count(i)
        s_ += co
    sum.append(s_)
    # print(s_)
print("Ss",sum)

# for i in range(len(arraylist_inkebkum)):
#     tmp = 0
#     for b in range(len(arraylist_kebkum)):
#         tmp += arraylist_inkebkum[i].count(arraylist_kebkum[b])
#     sum.append(tmp)
"""