class Solution(object):
    def intersect(self, nums1, nums2):
        i = 0
        j = len(nums2)
        print nums1[0:0]
        print nums1[i:j]
        
        while j < len(nums1):
            print nums1[i:j]
            if (nums1[i:j] == nums2):
                print "in while loop"
                return nums2
            i = i + 1
            j = j + 1


if __name__ == '__main__':
    s = Solution()
    print "the Intersection is : " + str(s.intersect([1,2], [1]))