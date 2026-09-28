class Solution:
    def maxDepth(self, s: str) -> int:
        depth,max_depth=0,0
        for i in s:
            if i=="(":
                depth+=1
                if max_depth<depth:
                    max_depth=depth
            elif i==")":
                depth-=1 
        return max_depth
        
      