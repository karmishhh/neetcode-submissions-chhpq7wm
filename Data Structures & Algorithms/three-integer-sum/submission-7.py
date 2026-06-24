class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums.sort()
        for idx in range(len(nums)):
            fixed = nums[idx]
            lookup_sum = -(fixed)
            left = idx+1
            right = len(nums) - 1
            while left < right:
                left_right_sum = nums[left] + nums[right]
                if left_right_sum < lookup_sum:
                    left += 1
                elif left_right_sum > lookup_sum:
                    right -= 1
                elif left_right_sum == lookup_sum:
                    res.add(tuple([nums[left], nums[right], fixed]))
                    left += 1
                    right -= 1

        return [list(x) for x in res]
                    


        