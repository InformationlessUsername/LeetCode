# 1. Two Sum
# https://leetcode.com/problems/two-sum/

# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Solution logic:
# Iterate through the list of numbers. For each number,
# add its index to a map of indices and values.
# Also calculate what number would be needed to be added to the current number in order to reach the target
# If this number is a key in the dictionary, return its value (the index of that number) along with the current index

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # dict (map) of numbers and what index they occur at in the list
        numbers_indexes = {}
        for index, num in enumerate(nums):
            # The number that would be needed to be added to the current number to equal the target number
            complement = target - num
            # If this complement has already been seen, it will be in the dict and we can return both indices
            if (complement) in numbers_indexes:
                return [numbers_indexes[complement], index]

            # Otherwise, add this number to the dict for the next iteration
            numbers_indexes[num] = index
