
def minimumSet(firstList,secondList):
    i = 0
    d = []
    firstList,secondList = zip(*sorted(zip(firstList,secondList)))

    d.append(secondList[0]-1)
    d.append(secondList[0])

    while (i<len(firstList)-1):
        counter = 0
        reverseCounter = -1
        if firstList[i+1]-secondList[i]<0:
            while counter<2:
                if d[reverseCounter] >=firstList[i+1] and d[reverseCounter]<=secondList[i+1]:
                    counter = counter + 1
                else:
                    d.append(secondList[i+1])
                    counter = counter +1
                reverseCounter = reverseCounter-1

        elif firstList[i+1]-secondList[i]>0:
            d.append(secondList[i+1]-1)
            d.append(secondList[i + 1])

        else:

            if d[-1] == firstList[i+1]:
                d.append(secondList[i+1])

            else:
                d.append(secondList[i+1]-1)
                d.append(secondList[i+1])
        i = i +1
    print d
    return len(d)





if __name__ == '__main__':
    print("solution is : " + str(minimumSet([0, 4, 5, 10],
                                            [4, 6, 9, 12])))

#     [0,1,2,3,4]
#             [4,5,6]
#               [5,6,7,8,9]
#                           [10,12]
# [3,4,6,9,10]
