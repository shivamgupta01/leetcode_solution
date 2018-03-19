n = 100
x = []
i = 0
while n>=i:
    arr = []
    sum = 0

    arr = list(str(i))
    arr.append(i)
    for j in arr:
        sum = sum + int(j)
    if sum<n:
        x.append(sum)
    i = i +1
print x


