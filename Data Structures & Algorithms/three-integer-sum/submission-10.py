class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for idx, val in enumerate(nums):
            required = -val
            left = idx+1
            right = len(nums)-1
            while left < right:
                positsum = nums[left] + nums[right]
                if positsum < required:
                    left += 1
                elif positsum > required:
                    right -= 1
                else: # we got 'em
                    res.add(tuple([nums[left], nums[right], val]))
                    left += 1
                    right -= 1
        
        return [list(x) for x in res]