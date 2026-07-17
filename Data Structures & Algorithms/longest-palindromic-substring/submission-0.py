class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = 0
        end = 0

        def getLength(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1 

        for i in range(len(s)):
            length = max(getLength(i, i), getLength(i, i+1))

            if length > end - start:
                print(i, length )
                start = i - (length-1) // 2
                end = i + length // 2
        
        return s[start:end+1]