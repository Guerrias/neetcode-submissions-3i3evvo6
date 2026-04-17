class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        longest = 0
        lastIndex = {}

        while right < len(s) :
            char = s[right]
            if char in lastIndex :
                left = max(left, lastIndex[char] + 1)
            lastIndex[char] = right
            right += 1
            longest = max(longest, right - left)
        return longest