from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        threshold = len(nums)//2
        for val in nums:
            if val in hashmap:
                hashmap[val] += 1
            else:
                hashmap[val] = 1
        
        newmap = {v:k for k,v in hashmap.items()}
        
        for val, _ in newmap.items():
            if val > threshold:
                return newmap.get(val)

        