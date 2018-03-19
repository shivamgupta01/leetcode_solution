def alert(inputs,windowSize,allowedIncrease):


    i = 0
    prevAllowedList = []
    prevAllowed = float(sum(inputs[0:windowSize]))/float(windowSize) * allowedIncrease
    prevAllowedList.append(prevAllowed)

    totalAverage = (float(sum(inputs))/float(windowSize))*allowedIncrease
    while(i+windowSize<=len(inputs)):
        currWindowAllowed = (float(sum(inputs[i:i + windowSize])) / float(windowSize) )*allowedIncrease
        currWindow = (float(sum(inputs[i:i + windowSize])) / float(windowSize) )
        # print prevAllowed,currWindow,currWindowAllowed
        # print prevAllowedList
        # print "*************************"

        if (currWindowAllowed < float(max(inputs[i:i+windowSize])) ) :
                return True
        for j in prevAllowedList:
            if j <currWindow:
                return True

        prevAllowed = float(sum(inputs[i:i+windowSize]))/float(windowSize)*allowedIncrease
        prevAllowedList.append(prevAllowed)
        # prevAllowedList.append(prevAllowed)
        i = i + 1

    return False

if __name__ == '__main__':
    print "the alerts is : " + str(alert([5,1,2,100,2,2],2,2.5))
    # print "the alerts is : " + str(alert([1,2,100,2,2],2,2.5))
    # print "the alerts is : " + str(alert([5,1,2,4,2,2],3,2.0))
    # print "the alerts is : " + str(alert([1,2,4,2,2],3,2.0))

