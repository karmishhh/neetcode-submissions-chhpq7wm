class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        left = 0
        right = row*column - 1
        while left <= right:
            mid = (left+right) // 2
            row_at = mid // column
            col_at = mid % column 
            if matrix[row_at][col_at] > target:
                right = mid - 1
            elif matrix[row_at][col_at] < target:
                left = mid + 1
            elif matrix[row_at][col_at] == target:
                return True
        return False