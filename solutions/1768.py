from typing import *
# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately/

# You are given two strings word1 and word2.
# Merge the strings by adding letters in alternating order, starting with word1.
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        return ''.join([(word1[i] if len(word1) > i else "") + (word2[i] if len(word2) > i else "") for i in range(max(len(word1), len(word2)))])
        merged = ""
        for i in range(max(len(word1), len(word2))):
            char1 = word1[i] if i < len(word1) else ""
            char2 = word2[i] if i < len(word2) else ""
            merged += char1 + char2
        return merged
