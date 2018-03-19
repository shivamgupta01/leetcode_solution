



class Solution:

    def passThrough(self,nums):
        print nums
        return True

if __name__ == '__main__':
    s = Solution()
    print "the answer is :" + str(s.passThrough([[0,1,1],[1,2,0],[2,1,1],[0,1,2]]))