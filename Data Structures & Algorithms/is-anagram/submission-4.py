class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_s = dict()
        hash_t = dict()
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hash_s[s[i]] = 1 + hash_s.get(s[i],0) # if key in dict then get its val and add 1 to it to mark duplicate
            hash_t[t[i]] = 1 + hash_t.get(t[i],0)
        
        return hash_s == hash_t

                

        
        