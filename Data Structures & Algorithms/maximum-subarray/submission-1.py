class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left = 0
        right = 0
        maxSum = - math.inf
        currSum = 0

        while right < len(nums):
            currSum += nums[right] 
            maxSum = max(currSum, maxSum)

            if currSum < 0:
                currSum = 0
                left = right +1
            
            right += 1
            
        return maxSum
        