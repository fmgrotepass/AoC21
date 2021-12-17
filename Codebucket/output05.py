import re
infile = open("input05.txt", "r")
#infile = open("input05ex.txt", "r")

#nums = [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1]
#infile = open("inputex4.txt", "r")
line = infile.readline()
coordsall=dict()
indexarr=0
cardcount = 0
while line:
    coordin = re.split("\s\-\>\s",line,1)
    print(line)
    coord0 = list(int(x) for x in coordin[0].split(","))
    coord1 = list(int(x) for x in coordin[1].split(","))
    
    if coord0[0] == coord1[0]:
        print("horizontal")
        for i in range(min(coord0[1], coord1[1]), max(coord0[1], coord1[1])+1):
            coordstr= ' '.join(map(str,[coord0[0],i]))
            if not len(coordsall) == 0:
                coordpos = coordsall.get(coordstr)
                if None == coordpos:
                    coordsall[coordstr]=1
                else:
                    coordsall[coordstr]=coordsall[coordstr]+1
            else:
                coordsall[coordstr]=1

    elif coord0[1] == coord1[1]:
        print("vertical")
        for i in range(min(coord0[0], coord1[0]), max(coord0[0], coord1[0])+1):
            coordstr= ' '.join(map(str,[i,coord0[1]]))
            if not len(coordsall) == 0:
                coordpos = coordsall.get(coordstr)
                if None == coordpos:
                    coordsall[coordstr]=1
                else:
                    coordsall[coordstr]=coordsall[coordstr]+1
            else:
                coordsall[coordstr]=1
    elif coord0[0]-coord1[0] == coord0[1]-coord1[1]:
        print("posDiag")
        rangedir=1
        if coord0[0] > coord1[0]:
            rangedir=-1
        print((rangedir+coord1[0]-coord0[0]))
        print(rangedir)
        for i in range(0, (rangedir+coord1[0]-coord0[0]), rangedir):
            coordstr= ' '.join(map(str,[coord0[0]+i,coord0[1]+i]))
            print(coordstr)
            if not len(coordsall) == 0:
                coordpos = coordsall.get(coordstr)
                if None == coordpos:
                    coordsall[coordstr]=1
                else:
                    coordsall[coordstr]=coordsall[coordstr]+1
            else:
                coordsall[coordstr]=1

    elif coord0[0]-coord1[0] == coord1[1]-coord0[1]:
        print("negDiag")
        rangedir=1
        if coord0[0] > coord1[0]:
            rangedir=-1
        print((rangedir+coord1[0]-coord0[0]))
        print(rangedir)
        for i in range(0, (rangedir+coord1[0]-coord0[0]), rangedir):
            coordstr= ' '.join(map(str,[coord0[0]+i,coord0[1]-i]))
            print(coordstr)
            if not len(coordsall) == 0:
                coordpos = coordsall.get(coordstr)
                if None == coordpos:
                    coordsall[coordstr]=1
                else:
                    coordsall[coordstr]=coordsall[coordstr]+1
            else:
                coordsall[coordstr]=1

    else:
        print("########################################squiffydiagonal")

    line = infile.readline()
   
pointsge2=0
pointslt2=0
for i in coordsall:
    if coordsall[i] > 1:
        pointsge2 +=1
    else:
        pointslt2 +=1

print(pointslt2)
print(pointsge2)


#
#
#
#
#
#
#
#
#
#    cardcount+=1
#    fullList.append([inarr0,inarr1,inarr2,inarr3,inarr4])
#    unmatchedList.append([[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1]])
#    line = infile.readline()
#
#for indexnum in range(len(nums)):
#    
#    found = 0
#    for i in range(cardcount):
#        foundicard = 0
##        print("index is {} with val {} on card {}".format(indexnum,nums[indexnum],i))
#        for j in range(5):
#            for k in range(5):
#                if fullList[i][j][k] == nums[indexnum]:
#                    if  not unmatchedList[i][j][k] == -2:
#                        unmatchedList[i][j][k] = nums[indexnum] 
#                        foundicard=1
##                    print("matched at {} {} {}".format(i,j,k))
##                    print(fullList[i])
##                    print(unmatchedList[i])
#
#        if foundicard == 1:
#            failC = [0,0,0,0,0]
#            failR = [0,0,0,0,0]
#            for j in range(5):
#                for k in range(5):
#                    if unmatchedList[i][j][k] == -1:
#                        failC[k] = 1
#                        failR[j] = 1
#            
#        
#            for j in range(5):
#                if failC[j] == 0:
#                    print("column {} passed for card {} and value {}".format(j,i,nums[indexnum]))
#                    print(fullList[i])
#                    print(unmatchedList[i])
#                    found=1 
#                if failR[j] == 0:
#                    print("row {} passed for card {} and value {}".format(j,i,nums[indexnum]))
#                    print(fullList[i])
#                    print(unmatchedList[i])
#                    found=1 
#            if found == 1:
#                unmarkedTot = 0
#                for j in range(5):
#                    for k in range(5):
#                        if unmatchedList[i][j][k] == -1:
#                            unmarkedTot += fullList[i][j][k]
#                        unmatchedList[i][j][k]=-2 # invalidate board
#                found = 0
#                print(unmatchedList[i])
#                print("unmarkedTotal {} for last match".format(unmarkedTot))
#
#                    
