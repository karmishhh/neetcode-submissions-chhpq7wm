class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = defaultdict(int)
        res = maxcount = 0
        for num in nums:
            hashmap[num] += 1
            res = num if hashmap[num] > maxcount else res
            maxcount = max(hashmap[num], maxcount)
        return res
        