import readfile as r
matrix = r.get_data("Coloring\data1.txt")
sizematrix = len(matrix)
def CoutPreaks(i):
    count = 0
    for j in range(sizematrix):
       if(matrix[i][j] == 1):
           count+=1
    return count
dict_matrix = {}
def AmountPearkAtIndex():
    dict_matrix = {}
    for i in range(sizematrix):
        dict_matrix[f"{i+1}"] = CoutPreaks(i)
    return dict_matrix

my_dict = AmountPearkAtIndex()
sorted_items = sorted(my_dict.items(), key=lambda x: x[1], reverse=True)
sorted_dict = dict(sorted_items)
Point = []
Point = list(map(int,sorted_dict.keys()))
print(Point)
def check_Ajactentpeak(i,j):
    if(matrix[Point[i]-1][j] == 1):
        return True
    return False
def IsInList(i,arr):
    for j in range(len(arr)):
        if(i == arr[j]):
            return True
    return False
numbercolor = 0
def coloring_graph():
    global numbercolor
    list_contain = []
    for i in range(sizematrix):
       list_contain.append(Point[i]-1)
       if IsInList(Point[i]-1,list_contain)==False:
            print("i",i)
            list_contain.append(Point[i]-1)
            for j in range(sizematrix):
                if  not matrix[Point[i]-1][j] == 1 and IsInList(j,list_contain)==False :
                    list_contain.append(j)
                    print(" abc " , j)

coloring_graph()
print(numbercolor)