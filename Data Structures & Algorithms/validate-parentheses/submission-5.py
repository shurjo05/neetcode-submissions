class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for c in s:
            if c in ['(','{','[']:
                stack.append(c)
            if c in [')','}',']']:
                if not stack:
                    return False
                check = stack[-1]
                if check == '(' and c == ')':
                    stack.pop()
                elif check == '{' and c == '}':
                    stack.pop()
                elif check == '[' and c == ']':
                    stack.pop()
                else:
                    return False
        return stack == []