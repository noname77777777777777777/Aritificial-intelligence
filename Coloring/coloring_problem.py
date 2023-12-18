import read_file as r
graph = r.get_data("Coloring\data1.txt")
class PairValue:
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2
    def getvalue(self):
        return self.value1,self.value2
    def setvalue(self,new_value1,new_value2):
        self.value1 = new_value1
        self.value2 = new_value2
    def getvalue1(self):
        return self.value1
    def getvalue2(self):
        return self.value2

PairList = []

def Count_adjacent_vertices(Graph,i):
    count = 0
    for j in range(len(Graph)):
        if(Graph[i][j] == 1):
            count+=1
    return count

def Add_adjacent_vertices(Graph,list):
    for i in range(len(Graph)):
        list.append(PairValue(i+1,Count_adjacent_vertices(Graph,i)))

Add_adjacent_vertices(graph,PairList)

Sort_List = sorted(PairList,key=lambda x: x.value2,reverse=True)

List_Color_Graph = []
def Get_Info_Color(SortList,ListColorGraph):
    for i in range(len(SortList)):
        #False is not colored ,vice versa
        ListColorGraph.append(PairValue(SortList[i].value1,False))
Get_Info_Color(Sort_List,List_Color_Graph)

def IsAdjacent(graph,i,j):
    return graph[i-1][j-1] == 0 and i!=j

def IsFullColorCheck(ListColorGraph):
    for i in range(len(ListColorGraph)):
        if(ListColorGraph[i].getvalue2 == False):
            return False
    return True

def Coloring_Problem(ListColorGraph,graph):
    IsFullColor = False
    while IsFullColor == False:
        for i in range(len(ListColorGraph)):
            if(IsFullColorCheck(ListColorGraph)):
                IsFullColor = True
            if(ListColorGraph[i].getvalue2 != True):
                print("1* " ,ListColorGraph[i].getvalue1())
                ListColorGraph[i].getvalue2 = True
                for j in range(len(graph)):
                    if(IsAdjacent(graph,int(ListColorGraph[i].getvalue1()),int(ListColorGraph[j].getvalue1())) and ListColorGraph[j].getvalue2!=True):
                        ListColorGraph[j].getvalue2 = True
                        print("2*  ",ListColorGraph[j].getvalue1())

Coloring_Problem(List_Color_Graph,graph)