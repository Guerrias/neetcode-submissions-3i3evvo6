class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) -1
        maxArea = 0

        while left < right :
            width = right - left
            if heights[left] > heights[right] :
                height = heights[right]
                right -= 1
            else :
                height = heights[left]
                left += 1
            maxArea = max(maxArea, height * width) 
        return maxArea