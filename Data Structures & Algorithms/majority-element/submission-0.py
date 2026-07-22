class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        max_count = len(nums)//2

        count_map = {}

        for num in nums:
            if num in count_map:
                count_map[num] += 1
                if count_map[num] > max_count:
                    return num
            else:
                count_map[num] = 1

        return nums[0]