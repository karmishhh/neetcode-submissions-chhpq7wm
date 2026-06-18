class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in hash:
                return sorted([i, hash.get(remaining)])
            else:
                hash[nums[i]] = i

        # for i in range(len(nums)):
            

        