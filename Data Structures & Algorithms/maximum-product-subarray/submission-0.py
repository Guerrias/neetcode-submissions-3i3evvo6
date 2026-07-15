class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = 1
        maxProd = 1
        res = -math.inf

        for num in nums:
            temp = max(minProd* num, max(maxProd * num, num))

            minProd = min(minProd* num, min(maxProd * num, num))
            maxProd = temp

            res = max(res, maxProd)
        return res