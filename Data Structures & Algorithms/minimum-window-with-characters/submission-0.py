class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s) :
             return ""
        
        freqT = {}
        freq = {}

        for char in t :
            freqT[char] = freqT.get(char, 0) + 1
        
        left = 0
        right = 0
        minWindowSize = len(s) + 1
        minLeft = -1
        minRight = -1

        #print(freqT)

        while right < len(s) :
            char = s[right]
            if char in freqT :
                freq[char] = freq.get(char, 0) + 1
            #print(freq)
            while freqT.keys() == freq.keys() and all(freq[k] >= freqT[k] for k in freqT) :
                #print(f"{minWindowSize} {right - left + 1}")
                if minWindowSize > right - left + 1 :
                    minWindowSize = right - left + 1
                    minLeft = left
                    minRight = right
                
                charToRemove = s[left]
                left += 1

                if charToRemove in freq :
                    freq[charToRemove] = freq.get(charToRemove, 0) -1
                
            right += 1
        return s[minLeft:minRight+1] if minLeft != -1 and minRight != -1 else ""
