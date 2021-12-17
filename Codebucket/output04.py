import re
nums = [27,14,70,7,85,66,65,57,68,23,33,78,4,84,25,18,43,71,76,61,34,82,93,74,26,15,83,64,2,35,19,97,32,47,6,51,99,20,77,75,56,73,80,86,55,36,13,95,52,63,79,72,9,10,16,8,69,11,50,54,81,22,45,1,12,88,44,17,62,0,96,94,31,90,39,92,37,40,5,98,24,38,46,21,30,49,41,87,91,60,48,29,59,89,3,42,58,53,67,28]
infile = open("input04.txt", "r")

#nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
#infile = open("inputex4.txt", "r")
line = infile.readline()
fullList = []
unmatchedList = []
indexarr=0
cardcount = 0
while line:
    inarr0 = list(int(x) for x in line.split())
    line = infile.readline()
    inarr1 = list(int(x) for x in line.split())
    line = infile.readline()
    inarr2 = list(int(x) for x in line.split())
    line = infile.readline()
    inarr3 = list(int(x) for x in line.split())
    line = infile.readline()
    inarr4 = list(int(x) for x in line.split())
    line = infile.readline()
    cardcount+=1
    fullList.append([inarr0,inarr1,inarr2,inarr3,inarr4])
    unmatchedList.append([[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]])
    line = infile.readline()

for indexnum in range(len(nums)):
    
    found = 0
    for i in range(cardcount):
        foundicard = 0
#        print("index is {} with val {} on card {}".format(indexnum,nums[indexnum],i))
        for j in range(5):
            for k in range(5):
                if fullList[i][j][k] == nums[indexnum]:
                    if  not unmatchedList[i][j][k] == -2:
                        unmatchedList[i][j][k] = nums[indexnum] 
                        foundicard=1
#                    print("matched at {} {} {}".format(i,j,k))
#                    print(fullList[i])
#                    print(unmatchedList[i])

        if foundicard == 1:
            failC = [0,0,0,0,0]
            failR = [0,0,0,0,0]
            for j in range(5):
                for k in range(5):
                    if unmatchedList[i][j][k] == -1:
                        failC[k] = 1
                        failR[j] = 1
            
        
            for j in range(5):
                if failC[j] == 0:
                    print("column {} passed for card {} and value {}".format(j,i,nums[indexnum]))
                    print(fullList[i])
                    print(unmatchedList[i])
                    found=1 
                if failR[j] == 0:
                    print("row {} passed for card {} and value {}".format(j,i,nums[indexnum]))
                    print(fullList[i])
                    print(unmatchedList[i])
                    found=1 
            if found == 1:
                unmarkedTot = 0
                for j in range(5):
                    for k in range(5):
                        if unmatchedList[i][j][k] == -1:
                            unmarkedTot += fullList[i][j][k]
                        unmatchedList[i][j][k]=-2 # invalidate board
                found = 0
                print(unmatchedList[i])
                print("unmarkedTotal {} for last match".format(unmarkedTot))

                    
