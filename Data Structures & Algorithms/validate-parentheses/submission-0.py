class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            print(stack)
            if len(stack) == 0:
                stack.append(c)
                continue
            if c == '}' or c == ')' or c == ']':
                if c == '}' and stack[-1] != '{':
                    return False
                elif c == ')' and stack[-1] != '(':
                    print('hor')
                    return False
                elif c == ']' and stack[-1] != '[':
                    return False
                else:
                    stack.pop()
            else: 
                stack.append(c)

        return len(stack) == 0
        