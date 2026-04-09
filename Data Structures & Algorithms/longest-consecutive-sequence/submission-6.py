class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        uniques = set(nums)
        longest = 1
        for val in uniques:
            if val-1 not in uniques:
                # its a start
                length = 1
                while val+length in uniques:
                    length += 1
                    longest = max(longest, length)
                
        return longest    