from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        
        hashmap = {}
        for string in strs:
            sortstr = ''.join(sorted(string))
            if sortstr in hashmap:
                hashmap[sortstr].append(string)
            else:
                hashmap[sortstr] = [string]
                        
        return list(hashmap.values())