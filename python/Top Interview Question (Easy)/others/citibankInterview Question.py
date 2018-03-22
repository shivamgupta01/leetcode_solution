a2 = [3,3,3,5,6,3]
a = [4,5,4,1,4,6,4,7,4]

set_a = set(a)
sum_total = 0
sum_individual = 0

for element in set_a:
    for i in a:
        if i == element or sum_individual<=len(a)/2:
            sum_individual = sum_individual+1
        elif sum_individual>len(a)/2:
            print element









