class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        numset = set(nums)
        longest = 1
        for num in numset:
            streak = 1
            i = 1
            while num-i in numset:
                streak += 1
                i += 1
            longest = max(longest, streak)
        return longest


        