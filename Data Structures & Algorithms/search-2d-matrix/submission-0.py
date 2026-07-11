class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0
        high = len(matrix) - 1
        candidate_row = []
        # identify the sub array in which the target might be present
        while low <= high:
            mid = (low+high)//2
            if matrix[mid][0] > target:
                high = mid - 1
            elif matrix[mid][0] < target:
                if matrix[mid][-1] < target:
                    low = mid + 1
                elif matrix[mid][-1] > target:
                    candidate_row = matrix[mid]
                    break
                else:
                    return True
            else:
                return True

        #once index is identified, we just do a normal binary search on the sub-array
        if candidate_row:
            low = 0
            high = len(candidate_row) - 1

            while low <= high:
                mid = (low+high)//2
                if candidate_row[mid] > target:
                    high = mid - 1
                elif candidate_row[mid] < target:
                    low = mid + 1
                else:
                    return True

        return False