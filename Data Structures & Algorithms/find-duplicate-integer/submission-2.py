class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True: # cycle toh hoga hi is question me humesha! 
            slow = nums[slow]
            fast = nums[fast]
            fast = nums[fast]
            if slow == fast: # meeting point, now we want to get to starting point 
                slow = 0
                while slow != fast:
                    slow = nums[slow]
                    fast = nums[fast]
                return slow 
# intuition - https://www.youtube.com/watch?v=jDP1NkjVjWQ
# solution - https://www.youtube.com/watch?v=RNpZBhZBtJc


            
                
