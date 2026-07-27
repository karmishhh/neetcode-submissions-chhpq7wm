class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numset = set(nums)
        for num in nums:
            streak, curr = 0, num
            while curr in numset:
                streak += 1
                curr += 1
            longest = max(longest, streak)
        return longest