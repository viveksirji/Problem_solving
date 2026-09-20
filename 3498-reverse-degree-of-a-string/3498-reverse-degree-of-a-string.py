class Solution:
    def reverseDegree(self, s: str) -> int:
        box={}
        j=1
        for i in range(122,96,-1):
            box[chr(i)]=j
            j+=1
        pos=1
        sum=0
        for ch in s:
            sum+=pos*box[ch]
            pos+=1
        return sum


        
   



        