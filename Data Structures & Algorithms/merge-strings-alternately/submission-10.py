class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        i = 0
        minlength = min(len(word1), len(word2))
        for i in range(minlength):
            res += word1[i]
            res += word2[i]
        res += word1[minlength:] 
        res += word2[minlength:]

        return res 