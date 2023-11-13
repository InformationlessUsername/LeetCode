from typing import *
# 605. Can Place Flowers
# https://leetcode.com/problems/can-place-flowers/

# You have a long flowerbed in which some of the plots are planted, and some are not.
# However, flowers cannot be planted in adjacent plots.

# Given an integer array flowerbed containing 0's and 1's,
# where 0 means empty and 1 means not empty, and an integer n,
# return true if n new flowers can be planted in the flowerbed
# without violating the no-adjacent-flowers rule and false otherwise.


# Solution Logic:
# Find the number of candies a kid would need to have pre-threshold to then have the most candies if given extraCandies
# Use a list comprehension to map int values to bool values dependent upon result of candy count comparison to threshold

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newly_potted = 0
        spaces = len(flowerbed)
        # Iterate through every index in the flowerbed
        for index, can_place in enumerate(flowerbed):
            # If already potted, skip
            if can_place == 1:
                continue

            # If the previous or next index are planted, skip
            prev_planted = flowerbed[index - 1] if index - 1 >= 0 else 0
            next_planted = flowerbed[index + 1] if index + 1 < spaces else 0
            if 1 in [prev_planted, next_planted]:
                continue

            flowerbed[index] = 1
            newly_potted += 1

        return newly_potted >= n
