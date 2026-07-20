class Solution:
    def findMin(self, nums: List[int]) -> int:
        minn = float('inf')
        left = 0
        right = len(nums)-1
        while left <= right:
            minn = min(minn, nums[left], nums[right])
            left += 1
            right -= 1
        return minn
        