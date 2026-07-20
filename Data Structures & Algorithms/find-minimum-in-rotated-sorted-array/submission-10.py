class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] > nums[right]: # means unsorted array
                left = mid + 1
            elif nums[mid] <= nums[right]: # means sorted array
                right = mid # search the left space - number is b/w left and the mid (including mid)
        return nums[left] # we return nums[right] since now left and right will be same so can do either lol  
            