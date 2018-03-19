matrix =[[0,-3,3],[0,-2,2],[0,-1,1]]

# Only change print to return below


m=0 # number of rows
n=0 # number of coloumns

sum_matrix = 0

for i in matrix:
    m = m +1
for i in matrix[0]:
    n = n +1
print  n, m

if n == 1 and m == 1:
    for i in matrix:
        for j in i:
            sum_matrix = sum_matrix +j
    print sum_matrix
    exit(0)

if m == 1:
    for i in matrix[0]:
        sum_matrix = sum_matrix + i
    print sum_matrix # return sum
    exit(0)


temp=[]
j = 0
sum_1 = 0

while j < m:
     temp.append([matrix[i][j] for i in range(len(matrix))])
     j = j +1
sum_temp = []
for i in temp:
    sum_temp.append(sum(i))
sum_temp = sorted(sum_temp)
i = 0
print sum_temp
while i<2:

    sum_temp[i]=sum_temp[i]*-1
    i = i + 1
print sum(sum_temp)