class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        res = [None] * len(s)

        def helper(s, start):
            if start >= len(s):
                return True
                
            if res[start] is not None:
                return res[start]
            
            for i in range(start +1, len(s)+1):
                if s[start:i] in wordSet and helper(s, i):
                    res[start] = True 
                    return res[start]
            
            res[start] = False
            return res[start]       
        return helper(s, 0)
