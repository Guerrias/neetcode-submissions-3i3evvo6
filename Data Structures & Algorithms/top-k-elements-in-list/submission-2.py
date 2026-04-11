class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            frequencies[num] = frequencies.get(num, 0) +1

        return sorted(frequencies, key=lambda x:frequencies[x], reverse = True)[:k]