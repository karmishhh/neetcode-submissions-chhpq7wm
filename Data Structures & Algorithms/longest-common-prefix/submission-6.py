class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        shortest = strs[0]
        for string in strs:
            if len(string) <= len(shortest):
                shortest = string
        
        for i in range(len(shortest)):
            for string in strs:
                if shortest[i] != string[i]:
                    return shortest[:i]
        return shortest
        