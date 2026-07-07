class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [1]*len(nums)

        prefix.append(1)
        postfix[-1] = 1
        for index in range(1, len(nums)):
            prefix.append(prefix[index-1]*nums[index-1])

        for index in range(len(nums)-2, -1, -1):
            postfix[index] = nums[index+1]*postfix[index+1]

        output = []
        for index in range(len(nums)):
            output.append(postfix[index]*prefix[index])

        return output