class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left] != s[right]:
                leftslice = s[left+1:right+1] # in slicing X[1:3] left is included and right index is excluded
                rightslice = s[left:right]

                return (leftslice == leftslice[::-1]) or (rightslice == rightslice[::-1])
            left += 1
            right -= 1
        return True
        