class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > nums[right]: # case 1 - crossover case
                if nums[left] <= target < nums[mid]: # target is in the left-mid block so search here hehehe 
                    right = mid - 1
                else: # target must be in the mid-right block so search there
                    left = mid + 1

            elif nums[mid] <= nums[right]: # case 2 - non crossover case
                if nums[mid] < target <= nums[right]: # target is in right block so move left
                    left = mid + 1 
                else:
                    right = mid - 1
        return -1