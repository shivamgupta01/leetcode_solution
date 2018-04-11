def solution(T,R):
    group = {}

    x = ''
    temp = []
    for t in T:
        i = 0
        x = ''
        while i < len(t):
            if t[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                x = x + t[i]
            i = i + 1
        temp.append(x)
    print temp

    i = 0
    while i <len(R):
        if temp[i] not in group and R[i] == 'ok':
            group[temp[i]] = 1
        elif temp[i] not in group and R[i] !='OK':
            group[temp[i]] = 0
        elif temp[i] in group and R[i] =='ok':
            if group[temp[i]]!=1:
                group[temp[i]] = 0
        i = i +1


    return int((sum(group.values())*100)/len(group))


print "the Result is :" + str(solution(['task1','task2a','task2b','task3','task4'],['worng answer','ok','ok','Wrong Answer','Worng Answer']))