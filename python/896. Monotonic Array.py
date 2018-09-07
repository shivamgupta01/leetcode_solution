'''An array is monotonic if it is either monotone increasing or monotone decreasing.

An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

Return true if and only if the given array A is monotonic.

'''

class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag_greater = True
        flag_smaller = True
        for i in range(len(A)-1):
            if A[i]>A[i+1]:
                flag_greater = False
            elif A[i] < A[i+1]:
                flag_smaller = False
        if flag_greater == False and flag_smaller == False:
            return False
        else:
            return True

        
if __name__ == '__main__':
    s = Solution()
    print(s.isMonotonic([1,2,2,1]))