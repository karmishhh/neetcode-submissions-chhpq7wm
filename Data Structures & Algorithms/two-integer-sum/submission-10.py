class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for idx, val in enumerate(nums):
            remaining = target - val
            if remaining in hash:
                return [hash.get(remaining), idx] # Since you populate the hash map as you move from left to right, the index already in the map will always be smaller than the current idx.
            else:
                hash[val] = idx
            

        