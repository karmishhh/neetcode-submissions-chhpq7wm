class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        if len(strs)==1:
            return [strs]
        
        for string in strs:
            sortstr = ''.join(sorted(string))
            if sortstr in hashmap:
                hashmap[sortstr].append(string)
            else:
                hashmap[sortstr] = [string]
        return list(hashmap.values())
