'''
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Note:

Each element in the result must be unique.
The result can be in any order.
'''

# One Liner solution:
# return list(set(nums1).intersection(set(nums2)))

class Solution:
    def intersection(self, nums1, nums2):
        dict_nums1 = {}
        dict_nums2 = {}

        for i in nums1:
            if i not in dict_nums1:
                dict_nums1[i] = True
        
        for i in nums2:
            if i not in dict_nums2:
                dict_nums2[i] = True
        if len(dict_nums2) > len(dict_nums1):
            return self.find_intersection(dict_nums1, dict_nums2)
        else:
            return self.find_intersection(dict_nums2, dict_nums1)

    def find_intersection(self,dict1,dict2):
        intersection = []
        for item in dict1.keys():
            if item in dict2.keys():
                intersection.append(item)
        return intersection
        

if __name__ == '__main__':
    s= Solution()
    print(s.intersection([4,9,5],[9,4,9,8,4]))

