from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            shash = defaultdict(int)
            thash = defaultdict(int)
            for i in range(len(s)):
                shash[s[i]] += 1
                thash[t[i]] += 1
        return shash == thash