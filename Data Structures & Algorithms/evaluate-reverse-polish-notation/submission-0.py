class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                param_2 = stack.pop()
                param_1 = stack.pop()
                if token == "+":
                    stack.append(param_1 + param_2)
                elif token == "-":
                    stack.append(param_1 - param_2)
                elif token == "*":
                    stack.append(param_1 * param_2)
                elif token == "/":
                    stack.append(int(param_1 / param_2))
        return stack.pop()