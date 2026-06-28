class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        traversed = {}
        for index, value in enumerate(nums):
            diff = target - value
            if diff in traversed:
                key = traversed[diff]
                return [key, index]
            traversed[value] = index
        return []