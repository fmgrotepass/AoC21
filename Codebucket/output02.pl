import re

infile = open("input02.txt", "r")
line = infile.readline()
forward = 0
aim = 0
depth  =0
while line:
    vars = re.split("\s",line,1)
    if (vars[0] == "forward"):
        forward +=int(vars[1], base=10)
        depth += aim*int(vars[1], base=10)
    if (vars[0] == "up"):
        aim -=int(vars[1], base=10)
    if (vars[0] == "down"):
        aim +=int(vars[1], base=10)
    line = infile.readline()

print(aim)
print(depth)
print(forward)
print(forward*(depth))

