class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        print(f"{nums}")
        for i, num in enumerate(nums):
            if i > 0 and nums[i-1] == nums[i]:
                continue
            self.twoSum(nums, result, i)
        return result

    def twoSum(self, nums: List[int], result: List[List[int]], start):
        left = start +1
        right = len(nums) -1

        while left < right:
            sum = nums[start] + nums[left] + nums[right]
            # print(f"{nums[start]} {nums[left]} {nums[right]} {sum}")
            if sum > 0 :
                right -= 1
            elif sum < 0 :
                left += 1
            else :
                result.append([nums[start], nums[left], nums[right]])
                left += 1
                right -= 1
                while left < right and nums[left] == nums[left-1]:
                    left += 1
                while left < right and nums[right] == nums[right+1]:
                    right -= 1
