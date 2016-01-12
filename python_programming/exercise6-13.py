# exercise6-13.py

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = int(strList[i])

def test():
    strList = ["239", "36", "938", "3746", "5", "93", "72949"]
    toNumbers(strList)
    print(strList)

test()
