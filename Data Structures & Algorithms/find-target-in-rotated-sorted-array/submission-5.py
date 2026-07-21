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


# NOTES!! 
# Breakdown of = Usage
# while left <= right: (A: Loop Condition)

# Why <=? This means the search continues as long as left and right either define a valid range (e.g., [0, 5]) or point to the same single element (e.g., [3, 3]). When left == right, mid will also be that index, and the loop checks nums[mid]. If the target isn't found, left will eventually become right + 1, and the loop terminates. This ensures that even the last potential element is checked.

# if nums[mid] == target: (B: Direct Hit Check)

# This is an exact equality, so no < or > involved. It's the first and most direct way to find the target.

# if nums[left] <= target < nums[mid]: (C: Target in Sorted Left Block)

# nums[left] <= target:

# Why <=? nums[left] is the starting point of the sorted segment. The target could potentially be equal to nums[left]. We haven't checked nums[left] explicitly as the target yet in this iteration (only nums[mid]). So, we must include it as a possibility.

# target < nums[mid]:

# Why < (exclusive)? nums[mid] has already been checked by the if nums[mid] == target: condition (B). If target were equal to nums[mid], we would have returned mid already. Therefore, when checking if target is in the segment, we only need to look for values strictly less than nums[mid].

# right = mid - 1 (D: Adjust Right Pointer)

# Why - 1? We know the target is in the [left, mid-1] range, and we've already checked nums[mid] (and confirmed it's not the target). So, we can safely exclude mid from the next search space.

# left = mid + 1 (E: Adjust Left Pointer)

# Why + 1? If the target is not in the [left, mid) range (checked in C), it must be in the [mid+1, right] range. We exclude mid because it's already checked and not the target.

# if nums[mid] < target <= nums[right]: (F: Target in Sorted Right Block)

# nums[mid] < target:

# Why < (exclusive)? Similar to point (C), nums[mid] has already been checked (B). If target were equal to nums[mid], we would have returned mid. So, we look for values strictly greater than nums[mid].

# target <= nums[right]:

# Why <=? nums[right] is the ending point of the sorted segment. The target could potentially be equal to nums[right]. We haven't checked nums[right] explicitly as the target yet. So, we must include it as a possibility.

# left = mid + 1 (G: Adjust Left Pointer)

# Why + 1? We know the target is in the [mid+1, right] range, and nums[mid] is not the target. So, exclude mid.

# right = mid - 1 (H: Adjust Right Pointer)

# Why - 1? If the target is not in the (mid, right] range (checked in F), it must be in the [left, mid-1] range. Exclude mid.

# General Rule of Thumb for Binary Search Boundaries:
# When checking if a target is within a defined [start, end] range:

# Use >= start if start itself hasn't been definitively ruled out as the target.

# Use < end if end itself has already been checked (e.g., mid).

# Use <= end if end itself has not yet been checked (e.g., right).

# When moving left or right pointers:

# Always use mid + 1 or mid - 1 if you are sure that nums[mid] is not the target. This helps prevent infinite loops by strictly shrinking the search space.

# Only use mid (e.g., right = mid) if nums[mid] could still be the target (e.g., in the "find minimum" problem where mid itself could be the minimum, and you are shrinking right to potentially land on mid).