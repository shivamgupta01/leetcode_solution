class Solution(object):
    def singleNumber(self, nums):
        nums =  sorted(nums)
        i =0
        while(i<len(nums)-1):
            if (nums[i]!=nums[i+1]):
                return nums[i]
            i = i +2
        if i == len(nums)-1:
            return nums[i]

if __name__ == '__main__':
    s=Solution();
    print "the answer is : " + str(s.singleNumber([1,2,3,4,5,6,7]))