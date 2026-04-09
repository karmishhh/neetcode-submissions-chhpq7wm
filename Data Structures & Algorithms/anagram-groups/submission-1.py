class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for word in strs:
            list_of_zeros = [0] * 26
            for char in word:
                numeric = ord(char) - ord('a')
                list_of_zeros[numeric] += 1

            key = tuple(list_of_zeros)

            if key in hashmap:
                hashmap[key].append(word)
            else:
                hashmap[key] = [word]

        
        return list(hashmap.values())

    


         