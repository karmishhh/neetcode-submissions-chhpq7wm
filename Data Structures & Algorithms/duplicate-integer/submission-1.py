class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash = {}
        for val in nums:
            if val in hash:
                hash[val] += 1
            else:
                hash[val] = 1
        for vals in hash.values():
            if vals != 1:
                return True
        return False



        