






class Solution(object):
    def calPoints(self,nums):
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
    print "the Score is : " + str(s.calPoints([6,5,5,6,8,8,5]))