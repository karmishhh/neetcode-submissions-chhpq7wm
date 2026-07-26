class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*2*n
        for i, val in enumerate(nums):
            res[i] = res[n+i] = val
        return res
        