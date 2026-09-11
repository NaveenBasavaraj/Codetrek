class Solution:
    def isValid(self, s: str) -> bool:
        closing_parentheses = {')':"(",
        "}":"{", "]":"["}
        stack = []
        for p in s:
            if p not in closing_parentheses:
                stack.append(p)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if top != closing_parentheses[p]:
                    return False
        return True if not stack else False