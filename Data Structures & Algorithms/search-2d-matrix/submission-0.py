class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        newlist = []
        for listt in matrix:
            for val in listt:
                newlist.append(val)
       
        left = 0
        right = len(newlist) - 1
        while left <= right:
            mid = (left + right) // 2 
            if newlist[mid] < target:
                left = mid + 1
            elif newlist[mid] > target:
                right = mid - 1
            else:
                return True
        return False

        