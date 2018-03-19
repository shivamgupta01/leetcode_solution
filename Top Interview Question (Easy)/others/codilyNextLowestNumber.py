

class Solution:

 def nextNum(self,A):
    A = sorted(set(A))
    i =1
    while i<=A[-1]:
        if i not in A:
            return i
        i +=1

    if A[-1]+1 >0:
        return A[-1]+1
    else:return 1



if __name__ == '__main__':
    s = Solution()
    print "The Solution is : " + str(s.nextNum([-1,-3]))