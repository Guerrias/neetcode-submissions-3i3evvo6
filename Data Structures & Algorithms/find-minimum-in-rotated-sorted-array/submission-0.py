class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minNum = 1001

        while left <= right :
            mid = left + (right - left)//2

            if nums[left] <= nums[mid] :
                minNum = min(minNum, nums[left])
                left = mid + 1
            else :
                minNum = min(minNum, nums[mid])
                right = mid -1
        return minNum
                