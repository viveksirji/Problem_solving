class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max=0
        for i in range (0,len(accounts)):
            localMax=0
            for j in range(0,len(accounts[0])):
                localMax+=accounts[i][j]
            if(localMax>max):
                max=localMax
        return max
        