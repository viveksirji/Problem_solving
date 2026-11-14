class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n=str(n)
        s,p=0,1
        for i in n:
            s+=int(i)
            p*=int(i)
        return p-s

        