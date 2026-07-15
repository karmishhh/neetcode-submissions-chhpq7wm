class Solution:

    def reverseee(self, left, right, nums):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        self.reverseee(0, len(nums)-1, nums)
        self.reverseee(0, k-1, nums)
        self.reverseee(k, len(nums)-1, nums)

        
        