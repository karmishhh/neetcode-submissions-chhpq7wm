class Solution:
    def is_palindrome(self, left, right, nums):
        while left <= right:
            if nums[left] != nums[right]:
                return False
            left += 1
            right -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left <= right:
            if s[left] != s[right]:
                return self.is_palindrome(left+1, right, s) or self.is_palindrome(left, right-1, s)   
            left += 1
            right -= 1
        return True