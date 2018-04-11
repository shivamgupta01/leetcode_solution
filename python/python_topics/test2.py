import  re
s ='task12a'
# l = re.compile("(?<!^)\s+(?=[A-Z])(?!.\s)").split(
i =0
x =''


while i<len(s):
    if s[i] in ['0','1','2','3','4','5','6','7','8','9']:
        while i <len(s):
            x  = x+s[i]
            i = i +1
    i = i +1


print x