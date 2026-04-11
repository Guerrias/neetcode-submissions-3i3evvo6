class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        occurence = {}
        for i, num in enumerate(nums):
            if num in occurence:
                return [occurence[num], i]
            occurence[target - num] = i
        return []