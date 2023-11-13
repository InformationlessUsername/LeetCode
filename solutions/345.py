from typing import *
# 345. Reverse Vowels of a String
# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Solution Logic:
# Use a list comprehension to filter the string down to vowels
# Treat that list of vowels like a stack. Loop through original string
# and replace vowels with vowel from stack (opposite order).

class Solution:
    def reverseVowels(self, s: str) -> str:
        # Define vowels
        vowels = ['a', 'e', 'i', 'o', 'u']
        # Add uppercase version of all letters
        vowels.extend([v.upper() for v in vowels])

        s_vowels = [char for char in s if char in vowels]
        # The below could be rewritten as:
        # return "".join([c if c not in vowels else s_vowels.pop(-1) for c in s])
        # but that is not easy to comprehend so a proper for loop is used

        new_s = ""
        for c in s:
            if c in vowels:
                new_s += s_vowels.pop(-1)
            else:
                new_s += c

        return new_s
