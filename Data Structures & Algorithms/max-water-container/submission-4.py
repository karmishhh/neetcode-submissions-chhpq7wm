class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxarea = 0
        left = 0
        right = len(heights)-1
        while left < right:
            length = min(heights[left], heights[right])
            breath = right - left
            area = length*breath
            maxarea = max(area, maxarea)

            if heights[left] < heights[right]: # then we move right since we can potentially increase the area since length will rise 
                left += 1
            elif heights[left] >= heights[right]: # In == case we can do either - increment left or decrement right, it will do same thing
                right -= 1
                

        return maxarea

