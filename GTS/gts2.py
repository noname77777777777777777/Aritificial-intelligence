import gts1
import sys
size = len(gts1.matrix)
def minGts():
    min_index =0
    min = gts1.GTS1(0,True)
    for i in range(size):
        if min >= gts1.GTS1(i,True):
            min = gts1.GTS1(i,True)
            min_index = i
    return min_index
def gts2():
    gts1.GTS1(minGts(),False)

gts2()