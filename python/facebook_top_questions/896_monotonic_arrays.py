'''
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

 

Example 1:

Input: [1,2,2,3]
Output: true
'''

class Solution:
    def isMonotonic(self, A):
        if len(A) in [1,2]:
            return True
        flag_increasing = True
        flag_decreasing = True
        i = 0

        while i < len(A) - 1:
            if A[i] < A[i + 1]:
                flag_decreasing = False
                if flag_increasing == False: return False
            elif A[i] > A[i + 1]:
                flag_increasing = False
                if flag_decreasing == False: return False
            i = i + 1
        
        return (flag_increasing or flag_decreasing)

if __name__ == "__main__":
    s = Solution()
    print(s.isMonotonic([1,2,2,3]))
        