class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = dict()
        hash_t = dict()
        for char in s:
            if char in hash_s:
                hash_s[char] += 1
            else:
                hash_s[char] = 1

        for char in t:
            if char in hash_t:
                hash_t[char] += 1
            else:
                hash_t[char] = 1

        return hash_s == hash_t
        
        