# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

# loop through nums list
        for sum1 in range(len(nums)):
            for sum2 in range(sum1+1, len(nums)):
                if nums[sum1] + nums[sum2] == target:
                    return [sum1, sum2]
        # condition isn't met with any of the elements, return None
                else:
                    return None