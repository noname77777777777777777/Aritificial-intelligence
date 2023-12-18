import readfile as matrixfile
import sys

matrix = matrixfile.get_data("GTS\data.txt")
maxnumber = sys.maxsize
sizematrix = len(matrix)
valueset = []        
sizevalue = len(valueset)
for i in range(sizematrix):
    for j in range(sizematrix):
        if i==j:
            matrix[i][j] = maxnumber
def getMin(i):
    for j in range(sizematrix):
        if j not in valueset:
            return matrix[i][j]
def FindMinValue(i):
    min = getMin(i)
    for j in range(sizematrix):
        if(j not in valueset):
            if(min >= matrix[i][j]):
                min = matrix[i][j]
    return min
def IndexMinValue(i):
    minvalue = FindMinValue(i)
    for j in range(sizematrix):
        if(matrix[i][j] == minvalue  ):
            return j
def CheckExtitsInListIndex(j):
    if j not in valueset:
        valueset.append(j)
def GTS1(index,isvalue):
    PriceMove = 0
    indexStrart = index
    valueset.append(indexStrart)
    if(isvalue == True):
        while(sizematrix != sizevalue):
            if FindMinValue(indexStrart) is None:
                PriceMove = PriceMove +  matrix[indexStrart][index]
                break
            else:
                PriceMove = PriceMove +  FindMinValue(indexStrart)
            indexStrart = IndexMinValue(indexStrart)
            CheckExtitsInListIndex(indexStrart)
            if indexStrart is None:
                break
        valueset.clear()
        return PriceMove
    else:
        print("Direction : ")
        while(sizematrix != sizevalue):
            print("->",indexStrart+1)
            print("Price ",PriceMove)
            if FindMinValue(indexStrart) is None:
                PriceMove = PriceMove +  matrix[indexStrart][index]
                break
            else:
                PriceMove = PriceMove +  FindMinValue(indexStrart)
            indexStrart = IndexMinValue(indexStrart)
            CheckExtitsInListIndex(indexStrart)
            if indexStrart is None:
                break
        print("->",index+1)
        print("Price : ", PriceMove)
        valueset.clear()
GTS1(6,False)