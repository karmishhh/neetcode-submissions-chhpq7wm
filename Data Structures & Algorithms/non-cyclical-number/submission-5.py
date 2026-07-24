class Solution:
    def findsum(self,n):
        summ = 0
        while n>0:
            d = n%10
            n = n//10
            summ += d*d
        return summ

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = n
        while fast != 1:
            slow = self.findsum(slow)
            fast = self.findsum(fast)
            fast = self.findsum(fast)
            if slow == fast and slow != 1: # we entered a cycle
                return False
        return True

# https://www.youtube.com/watch?v=RNpZBhZBtJc&t=1167s
