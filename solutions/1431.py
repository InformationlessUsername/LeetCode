from typing import *
# 1431. Kids With the Greatest Number of Candies
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/

# There are n kids with candies.
# You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has,
# and an integer extraCandies, denoting the number of extra candies that you have.

# Return a boolean array result of length n, where result[i] is true if,
# after giving the ith kid all the extraCandies,
# they will have the greatest number of candies among all the kids,
# or false otherwise.

# Note that multiple kids can have the greatest number of candies.


# Solution Logic:
# Find the number of candies a kid would need to have pre-threshold to then have the most candies if given extraCandies
# Use a list comprehension to map int values to bool values dependent upon result of candy count comparison to threshold

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        threshold = max(candies) - extraCandies
        return [candy >= threshold for candy in candies]
