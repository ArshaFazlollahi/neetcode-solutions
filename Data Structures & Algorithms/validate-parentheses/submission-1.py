class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["Range Guard"]
        for x in s:
            if x=='(' or x=='{' or x=='[':
                stack.append(x)
            if x==')':
                if stack[-1]!='(':
                    return False
                stack.pop()
            if x=='}':
                if stack[-1]!='{':
                    return False
                stack.pop()
            if x==']':
                if stack[-1]!='[':
                    return False
                stack.pop()
        stack.pop()
        if len(stack)!=0:
            return False
        return True