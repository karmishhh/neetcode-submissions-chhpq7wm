class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        for idx, val in enumerate(heights):
            left = idx
            right = len(heights)-1
            while left < right:
                length = min(heights[left], heights[right])
                breath = right - left
                area = length*breath
                maxarea = max(maxarea, area)
                right -= 1
        return maxarea
        