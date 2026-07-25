
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0]*2*n
        for idx, val in enumerate(nums):
            ans[idx] = ans[n+idx] = nums[idx]
        return ans

        