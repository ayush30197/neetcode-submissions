class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Brute Force - O(n^2)
        result =[]
        for index, value in enumerate(temperatures):
            found = False
            for j in range(index+1, len(temperatures)):
                if temperatures[j] > value:
                    result.append(j - index)
                    found = True
                    break
            if not found:
                result.append(0)

        return result