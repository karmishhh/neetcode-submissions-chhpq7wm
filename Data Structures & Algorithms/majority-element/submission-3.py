class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        threshold = len(nums)//2
        for val in nums:
            hashmap[val] = hashmap.get(val, 0) + 1
        
            if hashmap[val] > threshold:
                return val

        