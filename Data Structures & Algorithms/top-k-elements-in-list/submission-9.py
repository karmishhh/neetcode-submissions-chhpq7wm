class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        for val in nums:
            hashmap[val] += 1
        hashmap = dict(sorted(hashmap.items(), key = lambda x: x[1], reverse=True))
        return list(hashmap.keys())[:k]


        