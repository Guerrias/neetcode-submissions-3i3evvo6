class Solution:
    def numDecodings(self, s: str) -> int:
        res = [-1] * len(s)
        def numDecodingWay(s, idx):
            if idx == len(s):
                return 1
            
            if s[idx] == '0':
                return 0
            
            if res[idx] != -1:
                return res[idx]

            total = numDecodingWay(s, idx + 1)

            if idx + 1 < len(s) and int(s[idx:idx+2]) <= 26:
                total += numDecodingWay(s, idx +2)
            
            res[idx] = total
            return total
        
        return numDecodingWay(s, 0)