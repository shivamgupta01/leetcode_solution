

class Solution(object):
    def rotate(self, nums, k):
        newIndex = k % len(nums)
        nums = nums[newIndex+1:len(nums)] + nums[0:newIndex+1]
        print nums
        return nums

if __name__ == '__main__':
    s=Solution();
    print "the answer is : " + str(s.rotate([1,2,3,4,5,6,7], 3))