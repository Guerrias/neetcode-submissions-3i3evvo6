class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1]*len(nums)
        prod = 1
        for i, num in enumerate(nums):
            result[i] *= prod
            prod *= num

        prod = 1
        for i, num in reversed(list(enumerate(nums))):
            result[i] *= prod
            prod *= num
        
        return result