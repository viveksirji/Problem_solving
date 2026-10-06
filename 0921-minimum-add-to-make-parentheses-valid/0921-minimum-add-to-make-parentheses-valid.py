class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opn,add=0,0
        for char in s:
            if char=="(":
                opn+=1
            elif char==")":
                if opn>0:
                    opn-=1
                else:
                    add+=1
        return opn+add
        