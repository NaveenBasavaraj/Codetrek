"""
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
"""

class Solution:
    def isValid(self, s:str) -> bool:
        close_to_open_map = {
            "}":"{",
            ")":"(",
            "]":"["
        }
        stack = []
        for p in s:
            if p in close_to_open_map:
                # that means we started encountering closing brackets
                if stack and stack[-1] == close_to_open_map[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)
        return True if not stack else False

result = Solution()
print(result.isValid("[]")) # True
print(result.isValid("([{}])")) # True
print(result.isValid("[(])")) # False