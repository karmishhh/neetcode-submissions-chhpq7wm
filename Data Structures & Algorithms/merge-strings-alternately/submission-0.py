class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        rootlength = min(len(word1), len(word2))
        res = ''
        counter = 0
        for i in range(rootlength):
            res += word1[i] + word2[i]
            counter += 1

        if len(word1) > len(word2):
            remainingword = word1[counter:]
        else:
            remainingword = word2[counter:]
        
        return res + remainingword

            
        