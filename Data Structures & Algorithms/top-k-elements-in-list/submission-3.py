class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for val in nums:
            if val in hashmap:
                hashmap[val]+=1 
            else:
                hashmap[val] = 1
        
        arr = []
        for key, val in hashmap.items():
            arr.append([val, key])
        arr.sort()
        res = []
        while len(res) < k:
            res.append(arr.pop()[1])
        return res