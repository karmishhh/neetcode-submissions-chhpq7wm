from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        hashmap = defaultdict(list)
        for string in strs:
            sortstr = ''.join(sorted(string))
            hashmap[sortstr].append(string)  
        print(hashmap)           
        return list(hashmap.values())