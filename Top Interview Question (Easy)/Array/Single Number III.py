class Solution(object):
    def singleNumber(self, nums):
        nums =  sorted(nums)
        i =0
        temp = []
        while(i<len(nums)-1):
            if (nums[i]!=nums[i+1]):
                temp.append(nums[i])
                i = i -1
            i = i +2
        if i == len(nums)-1:
            temp.append(nums[i])
        return temp

if __name__ == '__main__':
    s=Solution();
    print "the answer is : " + str(s.singleNumber([1,2,3,4,5,6,7]))