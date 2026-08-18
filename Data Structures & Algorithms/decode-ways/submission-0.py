class Solution:
    def numDecodings(self, s: str) -> int:
        res = [-1] * len(s)
        def wayDecoding(s, idx):
            if idx == len(s):
                return 1

            if s[idx] == '0':
                return 0
            
            if res[idx] != -1:
                return res[idx]
                
            total = wayDecoding(s, idx + 1)

            if idx + 1 < len(s) and int(s[idx:idx+2]) <= 26:
                total += wayDecoding(s, idx + 2)
            
            res[idx] = total
            return total
        
        return wayDecoding(s, 0)