class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 1
        for right in range(1, len(nums)):
            if nums[right] != nums[right-1]: # found unique
                nums[left] = nums[right]
                left += 1
        return left
                
        # [1,1,2,3,4]
        # [2,10,10,30,30,30]
        # left = 2
        # right = 10 
        # right + 1 = 10 skip 
        # right + 1 = 30, yes. add it to prev right
        # left = 10 
        # 2, 10, 30
        # left = 10
        # right = 30
        # skip