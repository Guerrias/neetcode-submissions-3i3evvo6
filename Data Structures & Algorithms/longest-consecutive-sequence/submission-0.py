class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsSet = set(nums)
        for num in nums:
            if num -1 in numsSet:
                continue
            length = 1
            while num + length in numsSet:
                length += 1
            longest = max(longest, length)
        return longest