# # Find the Number of moves to select n-1 items in a go and Add 1 to each to make all element equal.
# input:
#
# 3,2,2,2
#
# Input
# 3 === Length of Array
# array.
#
# Output 0






class Solution(object):
    def CountMove(self,nums):
        flag = 0
        length = nums[0]
        nums = nums[1:]
        while (len(set(nums))!=1):
            nums.sort()
            new_list = [x + 1 for x in nums[:length - 1]]
            new_list.append(nums[length-1])
            nums=new_list
            flag = flag + 1
        return flag
if __name__ == '__main__':
    s = Solution()
    print "the Score is : " + str(s.CountMove([6,5,5,6,8,8,5]))