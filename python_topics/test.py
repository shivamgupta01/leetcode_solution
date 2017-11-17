def countMove(self, nums):
    flag = 0
    i = 0
    length = nums[0]
    nums = nums[1:]
    while (len(set(nums)) != 1):
        nums.sort()
        new_list = [x + 1 for x in nums[:length - 1]]
        new_list.append(nums[length - 1])
        nums = new_list
        flag = flag + 1
    return flag