class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for num in nums:
            current = num
            length = 1
            while (current + 1) in nums:
                length += 1 
                current += 1
            longest = max(longest, length)
        return longest