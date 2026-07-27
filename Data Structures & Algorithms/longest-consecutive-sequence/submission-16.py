class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        length = 1
        longest = 1
        nums.sort() # 2,3,4,5,10,20
        for i in range(1, len(nums)):
            if nums[i-1] not in nums:
                continue
            elif nums[i-1] == nums[i]:
                continue # handling duplicates
            elif nums[i] == nums[i-1] + 1:
                length += 1
            else:
                length = 1 # new sequence
            longest = max(longest, length)
        return longest


