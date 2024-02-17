class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == ')':
                if not stack or stack.pop()!="(":
                    return False
            elif item == ']':
                if not stack or stack.pop()!="[":
                    return False
            elif item == '}':
                if not stack or stack.pop()!="{":
                    return False
            else:
                stack.append(item)
        return not stack
        