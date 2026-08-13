class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        for num in nums:
            print(nums, num)
            idx = abs(num)
            if idx == len(nums) + 1:
                idx = 0
            
            if idx < len(nums):
                nums[idx] *= -1 
                if nums[idx] == 0:
                    nums[idx] = -(len(nums) + 1)
        
        
        for i, num in enumerate(nums):
            if num >= 0:
                return i
        
        return len(nums)