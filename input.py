import PyICU


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

word = 'บริษัท กานดาเคหะ จำกัด'
word = word.replace(" ","")
print(word)

kebkum2 = []
kebkum2.append(warp(word))
print(kebkum2)

arraylist_kebkum = []
arraylist_kebkum.append(kebkum2[0].split("|"))




#for c in range(len(kebkum2)):
    #cutkum[c] = kebkum2[c].split("|")
arraylist_kebkum = []
#print(warp(word))

