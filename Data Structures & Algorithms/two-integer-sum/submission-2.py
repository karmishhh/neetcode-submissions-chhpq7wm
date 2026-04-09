class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in nums and nums.index(remainder) != i:
                return sorted([nums.index(remainder),i])