class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, val in enumerate(nums):
            remaining = target - val
            if remaining in hash:
                return [hash.get(remaining), idx]
            else:
                hash[val] = idx
            

        