# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.

# Solution logic: 
# Create two pointers. Move right pointer from right to left. 
# Upon encountering an already-seen character, 
# move left pointer towards right until duplicates are removed
# Track largest gap achieved between two pointers. 
# That is the length of the largest substring without any repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        left_pointer = 0
        right_pointer = 0

        # The largest seen substring / distance between left and right pointers
        largest = 0

        # sets use dicts / maps, so they have O(1) time complexity
        # List of all the characters between and including left and right pointers
        seen = set()
        seen.add(s[0])

        while (right_pointer + 1) < len(s):
            # Move right pointer right
            right_pointer += 1
            right_char = s[right_pointer]
            left_char = s[left_pointer]

            if right_char in seen:
                # Move left pointer to the the previous instance of the right char.
                while left_char != right_char:
                    seen.remove(left_char)
                    left_pointer += 1
                    left_char = s[left_pointer]
                    
                # Move left pointer one right
                left_pointer += 1
            
            # Update tracked length of largest valid substring, if applicable
            largest = max(largest, right_pointer - left_pointer + 1)
            seen.add(right_char)

        return largest