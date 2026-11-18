class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for ch in s:
            if ch=="(" or ch=="{"or ch=="[":
                stack.append(ch)
            else:
                if len(stack)==0:
                    return False
                top=stack.pop()
                if ch=="]"and top!="[":
                    return False
                if ch=="}"and top!="{":
                    return False
                if ch==")"and top!="(":
                    return False
        if len(stack)==0:
            return True
        else:
            return False
















    #     stack = []
    #     for ch in s:
    #         if ch == '(' or ch == '{' or ch == '[':
    #             stack.append(ch)
    #         elif ch == ')':
    #             if not stack or stack[-1] != '(':
    #                 return False
    #             stack.pop()
    #         elif ch == '}':
    #             if not stack or stack[-1] != '{':
    #                 return False
    #             stack.pop()
    #         elif ch == ']':
    #             if not stack or stack[-1] != '[':
    #                 return False
    #             stack.pop()
    #     return len(stack) == 0


    # def isValid(self, s: str) -> bool:
    #     stack = []
    #     pairs = {
    #         ')': '(',
    #         '}': '{',
    #         ']': '['
    #     }
    #     for ch in s:
    #         if ch in pairs:
    #             if not stack or stack[-1] != pairs[ch]:
    #                 return False
    #             stack.pop()
    #         else:
    #             stack.append(ch)
    #     return len(stack) == 0





















