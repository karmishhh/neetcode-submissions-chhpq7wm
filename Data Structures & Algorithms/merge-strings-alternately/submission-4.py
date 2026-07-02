class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        if len(word1) > len(word2):
            rootlength = len(word2)
            remainder = word1
        else:
            rootlength = len(word1)
            remainder = word2
        res = ''
        for i in range(rootlength):
            res += word1[i] + word2[i]

        return res + remainder[rootlength:]

            
        