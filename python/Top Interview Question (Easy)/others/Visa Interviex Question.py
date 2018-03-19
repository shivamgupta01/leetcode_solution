# Jen coded a bot that takes a pair of integers coordinates, (x, y). Though the bot can move any
# number of times, it can only make the following two types of moves:
# 1. From location (x, y) to location (x + y, y).
# 2. From location (x, y) to location (x, x + y).


x1,y1=1,2
x2,y2=2,1
flag1 = False
flag2 = False
if x2 <x1 or y2<y1:
    print "no111"

while x2>=x1:

    if x2 ==x1:
        flag1 =True
        break
    x1 = x1 + y1

if flag1 == False:
    print "no22"

while y2 >= y1:

    if y2 == y1:
        flag2 = True
        print "YES11"
        break
    y1 = x1 + y1
print "NO333"











