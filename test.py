#!/usr/bin/python
#-*-coding: utf-8 -*-
import PyICU
import pymysql
import pymysql
conn = pymysql.connect(host='127.0.0.1', user='root', passwd='', db='projectone',charset = "utf8mb4")
# conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd=None, db='mysql')

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
    #print(warp(word))
    kebkum2.append(warp(word))
arraylist_kebkum = []
for c in kebkum2:

    arraylist_kebkum.append(c.split("|"))

print(arraylist_kebkum[0])