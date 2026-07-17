class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        def getLength(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            
            # -1 because both left and right will 1 step off of the actual palindrome
            # e.g for abab starting with left= 1 and right = 1, at the end of the loop 
            # left = -1 and right = 2
            return right - left - 1

        for i in range(len(s)):
            length = max(getLength(i, i), getLength(i, i+1))

            if length > end - start:
                start = i - (length-1) // 2
                end = i + length // 2
        
        return s[start: end+1]