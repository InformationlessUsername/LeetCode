from typing import *
# 151. Reverse Words in a String
# https://leetcode.com/problems/longest-palindromic-substring/

# Given an input string s, reverse the order of the words.
# A word is defined as a sequence of non-space characters.
# The words in s will be separated by at least one space.
# Return a string of the words in reverse order concatenated by a single space.
# Note that s may contain leading or trailing spaces or multiple spaces between two words.
# The returned string should only have a single space separating the words.
# Do not include any extra spaces.


# Solution Logic:
# Split the words using .split and reverse. Join into a string
# Use of these predefined methods is unique to high-level languages like Python

class Solution:
    def reverseWords(self, s: str) -> str:
        words = [w for w in s.strip().split(" ") if w not in [" ", ""]]
        reverse_words = [w.replace(" ", "") for w in words[::-1]]
        return " ".join(reverse_words)
