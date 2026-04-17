class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        longest = 0
        frequencies = {}
        maxFreq = 0

        for right in range(len(s)) :
            char = s[right]
            frequencies[char] = frequencies.get(char, 0) + 1
            maxFreq = max(maxFreq, frequencies[char])

            while right - left + 1 - maxFreq > k:
                char = s[left]
                frequencies[char] = frequencies.get(char) -1
                left += 1 

            longest = max(longest, right - left + 1) 
        return longest