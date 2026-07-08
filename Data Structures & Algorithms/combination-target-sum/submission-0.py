class Solution:
    def __init__(self):
        self.result = []
        
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        self.dfs(nums, target, [])
        return self.result

    def dfs(self, nums: List[int], target: int, temp: List[int]) -> None:
        if target == 0:
            self.result.append(temp[:])
            return
        if not nums or target < 0:
            return
        
        temp.append(nums[0])
        self.dfs(nums, target - nums[0], temp)
        temp.pop()
        self.dfs(nums[1:], target, temp)