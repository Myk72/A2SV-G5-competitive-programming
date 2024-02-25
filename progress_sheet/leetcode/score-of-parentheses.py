class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [] 
        res = 0 
        for idx, char in enumerate(s): 
            if char == '(': 
                stack.append(0)
            elif char == ')': 
                prev = stack.pop()
                # "(()(()))"
                if prev == 0: 
                    prev += 1 
                else: 
                    prev *= 2 
                #print(stack)
                if stack: 
                    stack[-1] += prev
                else: 
                    res += prev
        
        return res