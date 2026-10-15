class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        box=[]
        sq=[]
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                pairs=nums[i:j+1]
                box.append(pairs)
        counts = []
        for sub in box:
            counts.append(len(set(sub)))
        squares = [n ** 2 for n in counts]
        return sum(squares)

        


        