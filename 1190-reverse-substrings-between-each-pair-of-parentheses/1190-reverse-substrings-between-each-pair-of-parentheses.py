class Solution:
    def reverseParentheses(self, s: str) -> str:
        while "(" in s:
            close = 0
            for i in range(len(s)):
                if s[i] == ")":
                    close = i
                    break
            open = close
            while s[open] != "(":
                open -= 1
            part = s[open + 1:close]
            part = part[::-1]
            s = s[:open] + part + s[close + 1:]
        return s