
def minimumSet(firstList,secondList):
    i = 0
    d = []
    firstList=sorted(firstList)
    secondList = sorted(secondList)

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
            d.append(secondList[i+1])
            d.append(secondList[i+1]-1)

        else:
            d.append(secondList[i+1])

        i = i +1
    return len(d)





if __name__ == '__main__':
    print "solution is : " + str(minimumSet([1,4,7,9]
                                            ,[3,6,9,12]))