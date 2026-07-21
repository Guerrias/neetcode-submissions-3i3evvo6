class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * n for _ in range(n)]

        def dfs(curr, prev):
            if curr >= len(nums):
                return 0
            
            if memo[curr][prev] != -1:
                return memo[curr][prev]

            longest = dfs(curr+1, prev)

            if prev == -1 or nums[curr] > nums[prev]:
                longest = max(longest, 1 + dfs(curr + 1, curr))
            
            memo[curr][prev] = longest
            return longest
        return dfs(0, -1)