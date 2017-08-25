

def twoSums(nums,target):
           for i in range(len(nums)):
            for j in (range(len(nums))):
                #print j
                if (nums[i] + nums[j] == target):
                    if i != j:
                        return i,j

result = twoSums(nums=[3,2,4],target = 6)

print result





