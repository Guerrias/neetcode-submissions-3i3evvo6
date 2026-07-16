class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxAmount = [0] * (n+1)
        maxAmount[1] = nums[0]

        for i in range(2, n+1):
            maxAmount[i] = max(maxAmount[i-1], maxAmount[i-2] + nums[i-1])
        
        return maxAmount[n]