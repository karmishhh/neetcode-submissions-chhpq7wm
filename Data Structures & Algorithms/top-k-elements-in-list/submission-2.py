class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for val in nums:
            if val in hashmap:
                hashmap[val]+=1 
            else:
                hashmap[val] = 1
        
        top_keys = []
        
        if len(hashmap) == 1:
            return list(hashmap.keys())
        else:
            top_keys=[]
            max_values = list(sorted(hashmap.values())[::-1])[:k]
            for key,v in hashmap.items():
                if v in max_values:
                    top_keys.append(key)
            return top_keys




