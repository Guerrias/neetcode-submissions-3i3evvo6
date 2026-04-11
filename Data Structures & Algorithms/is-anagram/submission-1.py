class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        freqencies = [0] * 26
        for char in s:
            index = ord(char) - ord('a')
            freqencies[index] += 1

        for char in t:
            index = ord(char) - ord('a')
            freqencies[index] -= 1
            if freqencies[index] < 0:
                return False

        return True
