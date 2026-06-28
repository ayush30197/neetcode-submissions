class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        traversed_set = set()
        for i in nums:
            if i in traversed_set:
                return True
            traversed_set.add(i)
        return False