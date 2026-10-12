class Solution:
    def hammingWeight(self, n: int) -> int:
        count=0
        b=bin(n)
        for i in b:
            if i=="1":
                count+=1
        return count
        