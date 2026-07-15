class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverseee(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        k = k % len(nums)
        reverseee(0, len(nums)-1)
        reverseee(0, k-1)
        reverseee(k, len(nums)-1)

        
        