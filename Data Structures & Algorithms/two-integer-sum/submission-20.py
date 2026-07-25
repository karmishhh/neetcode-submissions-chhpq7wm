class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = [(idx, val) for idx, val in enumerate(nums)]
        indexed_nums.sort(key=lambda x: x[1])
        left = 0
        right = len(indexed_nums)-1 
        while left < right:
            currsum = indexed_nums[left][1] + indexed_nums[right][1] 
            if currsum > target:
                right -= 1
            elif currsum < target:
                left += 1
            else:
                left_idx = indexed_nums[left][0]
                right_idx = indexed_nums[right][0]
                return [min(left_idx, right_idx), max(left_idx, right_idx)]

        
        