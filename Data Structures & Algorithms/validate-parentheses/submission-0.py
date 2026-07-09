class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        stack = []
        match_set = {")":"(", "}":"{", "]":"["}
        for p in s:
            if p not in match_set :
                stack.append(p)
            elif not stack:
                return False
            else:
                expected = match_set[p]
                popped = stack.pop()
                if expected != popped:
                    return False

        if stack:
            return False
        return True