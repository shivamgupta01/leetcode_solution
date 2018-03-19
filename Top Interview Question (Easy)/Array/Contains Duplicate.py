class Solution(object):
    def containsDuplicate(self, nums):
        if len(set(nums)) != len(nums):
            return True
        else:
            return False
if __name__ == '__main__':
    s=Solution();
    print "the answer is : " + str(s.containsDuplicate([1,2,3,4,5,6,7]))
    