class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                skipleft = s[left+1:right+1]
                skipright = s[left:right]
                return skipleft == skipleft[::-1] or skipright == skipright[::-1]
            left += 1
            right -= 1
        return True
        