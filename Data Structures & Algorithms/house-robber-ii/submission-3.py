class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        memo = [[-1] * 2 for _ in range(len(nums))]

        def dfs(pos, flag):
            if pos >= len(nums) or (flag and pos == len(nums) - 1):
                return 0
            if memo[pos][flag] != -1:
                return memo[pos][flag]
            
            memo[pos][flag]= max(dfs(pos+1, flag), nums[pos] + dfs(pos +2, flag))
            return memo[pos][flag]
        
        return max(dfs(0, True), dfs(1, False))