class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for val in nums:
            if val in hash:
                hash[val] += 1
                return True
            else:
                hash[val] = 1
        return False