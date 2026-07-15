class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] == val:
                j = i+1
                while j < len(nums) :
                    if nums[j] != val:
                        temp = nums[j]
                        nums[j] = nums[i]
                        nums[i] = temp
                        k += 1
                        break
                    else:
                        j +=1
            else:
                k += 1
        return k