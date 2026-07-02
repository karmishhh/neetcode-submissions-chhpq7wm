class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rootlength = min(len(word1), len(word2))
        res = ''
        for i in range(rootlength):
            res += word1[i] + word2[i]
        return res + word1[rootlength:] + word2[rootlength:]
        