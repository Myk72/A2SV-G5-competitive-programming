class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for char in tokens:
            if char=="+":
                a=stack.pop()
                stack.append(int(a)+int(stack.pop()))
            elif char=="-":
                a=stack.pop()
                stack.append(int(stack.pop())-int(a))
            elif char=="*":
                a=stack.pop()
                stack.append(int(a)*int(stack.pop()))
            elif char=="/":
                a=stack.pop()
                stack.append(int(int(stack.pop())/int(a)))
            else:
                stack.append(int(char))
        return stack.pop()