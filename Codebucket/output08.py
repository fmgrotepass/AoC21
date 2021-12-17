import re
import copy

infile = open("input08.txt", "r")
#infile = open("inputex08.txt", "r")
#infile = open("input08min.txt", "r")

line = infile.readline()
coordsall=dict()
indexarr=0
digcount = 0
#digit=
#{
#    "0":[], # 6 segs - get
#    "1":[], # 2 segs
#    "2":[], # 5 segs - get
#    "3":[], # 5 segs - get
#    "4":[], # 4 segs
#    "5":[], # 5 segs - get
#    "6":[], # 6 segs - get
#    "7":[], # 3 segs
#    "8":[], # 7 segs
#    "9":[], # 6 segs - get
#    "a":[], # 7 - 1
#    "b":[], # 4 - 3 (5) of 4 - 9 (6) of 
#    "c":[], # 9 - 5 of 3 - 5 of 1 - 6 (6)
#    "d":[], # 4 - 0 (6)
#    "e":[], # 6 - 5
#    "f":[], # 1 - 2
#    "g":[], # 
#    }
tot=0
def getdiff(digit1, digit2):
    retlist=copy.deepcopy(digit1)
    if len(digit1) == 0 or len(digit2) == 0:
        return []

    for i in digit2:
        if i in retlist:
            retlist.remove(i)
    return retlist

def decstr(decodemap, encstr):
    print(decodemap)
    if len(encstr) == 2:
        return 1
    if len(encstr) == 3:
        return 7
    if len(encstr) == 4:
        return 4
    if len(encstr) == 7:
        return 8
    enclist=list(encstr)
    declist=[]
    for i in enclist:
        declist.append(decodemap[i])
    print("#################")
    print(declist)
    if len(declist) == 5:
        if 'c' in declist and 'f' in declist:
            return 3
        elif 'c' in declist:
            return 2
        else:
            return 5

    if len(declist) == 6:
        if not 'd' in declist:
            return 0
        elif not 'c' in declist:
            return 6
        else:
            return 9
    


while line:
    ssd = re.split("\s\|\s",line,1)
    ssdnum = re.split(" ",(ssd[1].strip('\n')),3)
    ssdenc = re.split(" ",(ssd[0].strip('\n')),9)

    secenc=dict()
    digits=dict()
    for i in ssdenc:
        if len(i) == 2:
            digits["1"]=list(i)
        elif len(i) == 3: 
            digits["7"]=list(i)
        elif len(i) == 4:
            digits["4"]=list(i)
        elif len(i) == 7:
            digits["8"]=list(i)
    secenc["a"]=getdiff(digits["7"],digits["1"])
    while (len(digits) + len(secenc)) < 15:
        for i in ssdenc:
            listi=list(i)
            #print(" list {} len {} and one min lsit {}".format(listi, len(i),getdiff(digits["1"],listi)))

            if len(i) == 6 and len(getdiff(digits["1"],listi)) == 1:
                digits["6"]=listi
                secenc["c"]=getdiff(digits["1"],listi)
                secenc["f"]=getdiff(digits["1"],secenc["c"])
                
            if len(i) == 5 and len(getdiff(digits["1"],listi)) == 0:
                digits["3"]=listi

            if "3" in digits and len(i) == 6 and len(getdiff(listi,digits["3"])) == 1:
                digits["9"]=listi
                secenc["e"]=getdiff(digits["8"],listi)
                secenc["b"]=getdiff(digits["4"],digits["3"])

            if "e" in secenc and len(i) == 5 and len(getdiff(secenc["e"], listi)) == 1:
                digits["5"]=listi
                secenc["g"]=getdiff(getdiff(digits["5"],digits["4"]),secenc["a"])
            if "3" in digits and "g" in secenc:
                tmplist=getdiff(digits["3"],digits["7"]) #dg
                secenc["d"]=getdiff(tmplist,secenc["g"])
     
    segdec=dict()
    for i in secenc:
        print(i)
        segdec[' '.join(secenc[i])]=i
    print(decstr(segdec,ssdnum[0])) 
    internalnum = decstr(segdec,ssdnum[0]) * 1000 + decstr(segdec,ssdnum[1]) * 100 + decstr(segdec,ssdnum[2]) * 10 + decstr(segdec,ssdnum[3]) 
    tot += internalnum
    print(internalnum)

    #print(segs)
    #    print(segs)
    line = infile.readline()
print(tot)    
#    coord0 = list(int(x) for x in coordin[0].split(","))
#    coord1 = list(int(x) for x in coordin[1].split(","))
#    
#    if coord0[0] == coord1[0]:
#        print("horizontal")
#        for i in range(min(coord0[1], coord1[1]), max(coord0[1], coord1[1])+1):
#            coordstr= ' '.join(map(str,[coord0[0],i]))
#            if not len(coordsall) == 0:
#                coordpos = coordsall.get(coordstr)
#                if None == coordpos:
#                    coordsall[coordstr]=1
#                else:
#                    coordsall[coordstr]=coordsall[coordstr]+1
#            else:
#                coordsall[coordstr]=1
#
#    elif coord0[1] == coord1[1]:
#        print("vertical")
#        for i in range(min(coord0[0], coord1[0]), max(coord0[0], coord1[0])+1):
#            coordstr= ' '.join(map(str,[i,coord0[1]]))
#            if not len(coordsall) == 0:
#                coordpos = coordsall.get(coordstr)
#                if None == coordpos:
#                    coordsall[coordstr]=1
#                else:
#                    coordsall[coordstr]=coordsall[coordstr]+1
#            else:
#                coordsall[coordstr]=1
#    elif coord0[0]-coord1[0] == coord0[1]-coord1[1]:
#        print("posDiag")
#        rangedir=1
#        if coord0[0] > coord1[0]:
#            rangedir=-1
#        print((rangedir+coord1[0]-coord0[0]))
#        print(rangedir)
#        for i in range(0, (rangedir+coord1[0]-coord0[0]), rangedir):
#            coordstr= ' '.join(map(str,[coord0[0]+i,coord0[1]+i]))
#            print(coordstr)
#            if not len(coordsall) == 0:
#                coordpos = coordsall.get(coordstr)
#                if None == coordpos:
#                    coordsall[coordstr]=1
#                else:
#                    coordsall[coordstr]=coordsall[coordstr]+1
#            else:
#                coordsall[coordstr]=1
#
#    elif coord0[0]-coord1[0] == coord1[1]-coord0[1]:
#        print("negDiag")
#        rangedir=1
#        if coord0[0] > coord1[0]:
#            rangedir=-1
#        print((rangedir+coord1[0]-coord0[0]))
#        print(rangedir)
#        for i in range(0, (rangedir+coord1[0]-coord0[0]), rangedir):
#            coordstr= ' '.join(map(str,[coord0[0]+i,coord0[1]-i]))
#            print(coordstr)
#            if not len(coordsall) == 0:
#                coordpos = coordsall.get(coordstr)
#                if None == coordpos:
#                    coordsall[coordstr]=1
#                else:
#                    coordsall[coordstr]=coordsall[coordstr]+1
#            else:
#                coordsall[coordstr]=1
#
#    else:
#        print("########################################squiffydiagonal")
#
#    line = infile.readline()
#   
#pointsge2=0
#pointslt2=0
#for i in coordsall:
#    if coordsall[i] > 1:
#        pointsge2 +=1
#    else:
#        pointslt2 +=1
#
#print(pointslt2)
#print(pointsge2)


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
