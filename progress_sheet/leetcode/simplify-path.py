class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        stack = []
        for item in s:
            if item == "..":
                if stack:
                    stack.pop()
            elif item!="" and item!=".":
                stack.append(item)
        return "/" + "/".join(stack)