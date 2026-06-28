class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        traversed = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in traversed:
                return [traversed[diff], index]
            traversed[value] = index
        return []