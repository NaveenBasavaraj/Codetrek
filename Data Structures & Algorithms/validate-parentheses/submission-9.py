class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open_map = {
            ")":"(",
            "]":"[",
            "}":"{"
        }

        stack = []

        for p in s:
            if p in close_to_open_map:
                # that means its a closing bracket
                if stack and stack[-1] == close_to_open_map[p]:
                    stack.pop()
                else:
                    return False
            else:
                # its an opening bracket
                stack.append(p)
        return True if not stack else False