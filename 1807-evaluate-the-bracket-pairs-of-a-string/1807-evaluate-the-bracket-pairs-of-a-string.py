class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        d = {}
        for pair in knowledge:
            d[pair[0]] = pair[1]
        result = ""
        i = 0
        while i < len(s):
            if s[i] != '(':
                result += s[i]
                i += 1
            else:
                i += 1
                key = ""
                while s[i] != ')':
                    key += s[i]
                    i += 1
                if key in d:
                    result += d[key]
                else:
                    result += '?'
                i += 1
        return result