class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        total = 0
        for op in operations:
            if op == "+":
                s = result[-1] + result[-2]
                result.append(s)
                total += s
            elif op == "C":
                val = result.pop()
                total -= val
            elif op == "D":
                m = result[-1]*2
                result.append(m)
                total += m
            else:
                result.append(int(op))
                total += int(op)

        return total