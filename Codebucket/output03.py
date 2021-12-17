import re

def oxFromList(inList, mask):
    outList = []
    count1=0
    count0=0
    for i in inList:
        if i & mask:
            count1+=1
        else:
            count0+=1
    for i in inList:
        if (count1 >= count0):
            if i & mask:
                outList.append(i)
        else:
            if not (i & mask):
                outList.append(i)
    return outList

def coFromList(inList, mask):
    outList = []
    count1=0
    count0=0
    for i in inList:
        if i & mask:
            count1+=1
        else:
            count0+=1
    for i in inList:
        if (count1 < count0):
            if i & mask:
                outList.append(i)
        else:
            if not (i & mask):
                outList.append(i)
    return outList


        

bit0=0
bit1=0
bit2=0
bit3=0
bit4=0
bit5=0
bit6=0
bit7=0
bit8=0
bit9=0
bit10=0
bit11=0

mask00=0b100000000000
mask01=0b010000000000
mask02=0b001000000000
mask03=0b000100000000
mask04=0b000010000000
mask05=0b000001000000
mask06=0b000000100000
mask07=0b000000010000
mask08=0b000000001000
mask09=0b000000000100
mask10=0b000000000010
mask11=0b000000000001
infile = open("input03.txt", "r")
#infile = open("inputex3.txt", "r")
line = infile.readline()
fullList = []

while line:
    inval = int(line, base=2)
    fullList.append(inval) 
    line = infile.readline()

oxlist0 = oxFromList(fullList,mask00)
oxlist1 = oxFromList(oxlist0,mask01)
oxlist2 = oxFromList(oxlist1,mask02)
oxlist3 = oxFromList(oxlist2,mask03)
oxlist4 = oxFromList(oxlist3,mask04)
oxlist5 = oxFromList(oxlist4,mask05)
oxlist6 = oxFromList(oxlist5,mask06)
oxlist7 = oxFromList(oxlist6,mask07)
oxlist8 = oxFromList(oxlist7,mask08)
oxlist9 = oxFromList(oxlist8,mask09)
oxlist10 = oxFromList(oxlist9,mask10)
oxlist11 = oxFromList(oxlist10,mask11)
print(oxlist0)
print(oxlist1)
print(oxlist2)
print(oxlist3)
print(oxlist4)
print(oxlist5)
print(oxlist6)
print(oxlist7)
print(oxlist8)
print(oxlist9)
print(oxlist10)
print(oxlist11)
colist0 = coFromList(fullList,mask00)
colist1 = coFromList(colist0,mask01)
colist2 = coFromList(colist1,mask02)
colist3 = coFromList(colist2,mask03)
colist4 = coFromList(colist3,mask04)
colist5 = coFromList(colist4,mask05)
colist6 = coFromList(colist5,mask06)
colist7 = coFromList(colist6,mask07)
colist8 = coFromList(colist7,mask08)
colist9 = coFromList(colist8,mask09)
colist10 = coFromList(colist9,mask10)
colist11 = coFromList(colist10,mask11)
print(colist0)
print(colist1)
print(colist2)
print(colist3)
print(colist4)
print(colist5)
print(colist6)
print(colist7)
print(colist8)
print(colist9)
print(colist10)
print(colist11)
gamma = 0
eps = 0
if(bit0 > 0):
    gamma += mask00
else:
    eps += mask00
if(bit1 > 0):
    gamma += mask01
else:
    eps += mask01
if(bit2 > 0):
    gamma += mask02
else:
    eps += mask02
if(bit3 > 0):
    gamma += mask03
else:
    eps += mask03
if(bit4 > 0):
    gamma += mask04
else:
    eps += mask04
if(bit5 > 0):
    gamma += mask05
else:
    eps += mask05
if(bit6 > 0):
    gamma += mask06
else:
    eps += mask06
if(bit7 > 0):
    gamma += mask07
else:
    eps += mask07
if(bit8 > 0):
    gamma += mask08
else:
    eps += mask08
if(bit9 > 0):
    gamma += mask09
else:
    eps += mask09
if(bit10 > 0):
    gamma += mask10
else:
    eps += mask10
if(bit11 > 0):
    gamma += mask11
else:
    eps += mask11

print(bit0)
print(bit1)
print(bit2)
print(bit3)
print(bit4)
print(bit5)
print(bit6)
print(bit7)
print(bit8)
print(bit9)
print(bit10)
print(bit11)
print("{:012b}".format(gamma))
print("{:012b}".format(eps))
print(eps)
print(gamma)
print(eps)
print(gamma*eps)




