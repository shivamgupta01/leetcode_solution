'''
Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
'''
import random
class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.temp_array = nums  
        self.original = list(nums)  
        

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        # for key,value in self.original_index.items():
        #     self.nums[key] = value
        # self.temp_nums = list(self.nums)
        self.temp_array = self.original
        self.original = list(self.original)
        return self.temp_array


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        for i in range(len(self.temp_array)):
            new_index = random.randrange(i,len(self.temp_array))
            self.temp_array[i], self.temp_array[new_index] =\
                    self.temp_array[new_index],self.temp_array[i]
        return self.temp_array

# Your Solution object will be instantiated and called as such:
obj = Solution([-6,10,184])
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
print(obj.shuffle())
print(obj.reset())
