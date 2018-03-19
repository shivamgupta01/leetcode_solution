class Solution:
    def uniqueWindow(self, nums):
        uniqueNumberLength = len(set(nums))
        tempLenght = []

        temp_dic = {}
        i = 0
        j = i

        while (i < len(nums)):
            if len(temp_dic) < uniqueNumberLength:
                if nums[i] not in temp_dic:
                    temp_dic[nums[i]] = 1
            else:
                tempLenght.append(i - j)
                j = j + 1
                i = j

                temp_dic = {}
            i += 1
        return min(tempLenght)


if __name__ == '__main__':
    s = Solution()
    print "Solution is: " + str(s.uniqueWindow([1, 2, 3, 4, 4, 4, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3]))


 # if len(set(nums)) == len(nums):
        #     return len(nums)
# try:
#     return min(tempLenght)
# except:
#     return uniqueNumberLength