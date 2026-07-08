class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            curr_area = (j-i)*min(heights[j], heights[i])
            if max_area < curr_area:
                max_area = curr_area
            if heights[j] > heights[i]:
                i += 1
            else:
                j -= 1

        return max_area