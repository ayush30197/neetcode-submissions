class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result =[0]*(len(temperatures))
        my_stack = []
        n = len(temperatures)
        for i in range(n):
            while my_stack:
                top, index = my_stack[-1]
                if top < temperatures[i]:
                    my_stack.pop()
                    result[index] = i - index
                else:
                    break
            my_stack.append((temperatures[i], i))
        return result