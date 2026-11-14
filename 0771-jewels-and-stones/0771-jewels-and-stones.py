class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count=0
        for i in stones:
            for j in jewels:
                if i==j:
                    count+=1
        return count
        