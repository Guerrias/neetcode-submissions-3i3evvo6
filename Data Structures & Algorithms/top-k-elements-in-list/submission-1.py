class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = defaultdict(int)
        unique_nums = []
        for num in nums:
            if frequencies[num] == 0:
                unique_nums.append(num)
            frequencies[num] += 1

        unique_nums.sort(key=lambda x:frequencies[x])
        return unique_nums[len(unique_nums) - k:]