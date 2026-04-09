class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        shortest_str = strs[0]
        for strr in strs:
            if len(strr) < len(shortest_str):
                shortest_str = strr

        for i in range(len(shortest_str)):
            for string in strs:
                if string[i] != shortest_str[i]:
                    return prefix
                else:
                    print(shortest_str[i], string[i])
            prefix += shortest_str[i]
        return prefix
                    
         