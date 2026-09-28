class Solution:
    def maxDepth(self, s: str) -> int:
        depth,td=0,0
        for i in s:
            if i=="(":
                depth+=1
                if depth>td:
                    td=depth
            elif i==")":
                depth-=1
        return td

            