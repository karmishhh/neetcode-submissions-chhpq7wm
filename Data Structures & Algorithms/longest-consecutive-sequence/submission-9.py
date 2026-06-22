class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0
        for val in nums:
            if (val-1) not in numset: # we found start of sequence
                length = 0 # to get the current
                while (val+length) in numset:
                    length += 1
                longest = max(length, longest)
        return longest 
            

        