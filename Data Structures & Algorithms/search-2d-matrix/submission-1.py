class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # brute force
        one_d_list = []
        for outer_list_items in matrix:
            for inner_list_items in outer_list_items:
                one_d_list.append(inner_list_items)

        low = 0
        high = len(one_d_list) - 1
        while low <= high:
            mid = (low + high)//2
            if one_d_list[mid] < target:
                low = mid + 1
            elif one_d_list[mid] > target:
                high = mid - 1
            else:
                return True
        return False