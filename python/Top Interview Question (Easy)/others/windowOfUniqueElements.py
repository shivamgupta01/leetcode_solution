class Solution:

 def uniqueWindow(self,nums):
     uniqueNumberLength = len(set(nums))
     tempLength = le


     temp_dic = {}
     i = 0
     j = i
     while(i<len(nums)):
         if len(temp_dic)<uniqueNumberLength:
             if nums[i] not in temp_dic:
                 temp_dic[nums[i]] = 1
         else:
             if tempLength <i-j:
                 tempLength = i-j
             i = j
             j = j +1
             temp_dic ={}
         i +=112
     try:
        return tempLength
     except:
         return uniqueNumberLength



if __name__ == '__main__':
    s = Solution()
    print "Solution is: "+str(s.uniqueWindow([7, 3, 7, 3, 1, 3, 4, 1]))

