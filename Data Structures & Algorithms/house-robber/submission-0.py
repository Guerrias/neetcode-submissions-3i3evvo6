class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        maxAmount = [0] * (n+1)
        maxAmount[1] = nums[0]

        for i in range(2, n+1):
            maxAmount[i] = maxAmount[i-1]
            if i >= 2:  
                maxAmount[i] = max(maxAmount[i-1], maxAmount[i-2] + nums[i-1])
        return maxAmount[n]

        
        """
        def recursion(nums, pos) -> List[int]:
            if pos >= len(nums):
                return [0, 0]
            
            include = nums[pos] + recursion(nums, pos +1)[1]
            result = recursion(nums, pos + 1)

            return [include, max(result[0], result[1])]
        
        result = recursion(nums, 0)
        return max(result[0], result[1])
        """