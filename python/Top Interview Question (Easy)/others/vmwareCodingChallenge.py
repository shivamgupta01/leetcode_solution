class Solution:

    def passThrough(self,maria,andrea,s):

        i = 0
        mariaScore = 0
        andreaScore = 0

        if (s == 'odd'):
            i = i +1

        while(i<len(maria)):
            andreaScore += andrea[i]-maria[i]
            mariaScore += maria[i]-andrea[i]

            i = i+2


        if andreaScore>mariaScore:
            return 'Andrea'
        elif mariaScore>andreaScore:
            return 'Maria'
        else:
            'Tie'

if __name__ == '__main__':
    s = Solution()
    print "the answ:" + str(s.passThrough([3,1,2,3],[3,2,1,3]))