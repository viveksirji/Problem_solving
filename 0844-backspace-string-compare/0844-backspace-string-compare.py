class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        ss,tt=[],[]
        for i in s:
            if i!="#":
                ss.append(i)
            elif ss:
                ss.pop()
        for i in t:
            if i!="#":
                tt.append(i)
            elif tt:
                tt.pop()
        return ss==tt
        

        