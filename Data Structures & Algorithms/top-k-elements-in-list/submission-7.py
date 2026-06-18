class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        res = []
        for val in nums:
            if val in hashmap:
                hashmap[val] += 1
            else:
                hashmap[val] = 1
        # print(hashmap)
        sorted_map = sorted(hashmap.items(), key=lambda x:x[1])
        while len(res)<k:
            res.append(sorted_map.pop()[0])
        return res






            # {1: 1, 2: 1, 3:10}

            # values -> 10,1 
            # return 3 and ALL keys associated with that value

        ## sort the dictionary by values and then get the keys associated with them 
        

        