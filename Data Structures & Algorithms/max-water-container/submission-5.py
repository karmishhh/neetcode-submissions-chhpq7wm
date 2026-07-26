class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(heights)-1
        while left < right:
            length = min(heights[left], heights[right])
            breath = right - left
            area= length*breath
            maxarea = max(area, maxarea)
            
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] >= heights[right]:
                right -= 1
        return maxarea

            