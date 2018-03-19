

class Solution:

 def bikeRack(self,nums):

    sorted_nums = sorted(nums)


    max_dist = 0
    i =0
    while (i<len(nums)-1):
        max_dist = max(nums[i+1]-nums[i],max_dist)
        i=i+1

    return max_dist/2

if __name__ == '__main__':
    s = Solution()
    print "Solution is : " + str(s.bikeRack([]))
