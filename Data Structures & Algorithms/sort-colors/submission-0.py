class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        total_slots = max(nums) + 1
        counts = [0]*total_slots

        for value in nums:
            counts[value] += 1

        i = 0
        for index, v in enumerate(counts):
            for j in range(v):
                nums[i] = index
                i += 1