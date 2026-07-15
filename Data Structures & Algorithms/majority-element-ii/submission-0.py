class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        res = []
        threshold = len(nums)//3
        hashmap = defaultdict(int)
        for val in nums:
            hashmap[val] += 1
        for k,v in hashmap.items():
            if v > threshold:
                res.append(k)
        return res
        
