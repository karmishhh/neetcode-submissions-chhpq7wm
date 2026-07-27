class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        i = 0
        j = 0
        minlength = min(len(word1), len(word2))
        counter = 0
        for i in range(minlength):
            res += word1[i]
            res += word2[i]
            counter += 1

        res += word1[counter:] 
        res += word2[counter:]

        return res 