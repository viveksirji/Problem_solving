class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        d={}
        for i in nums:
            if i>0:
                d[i]=1
        for i in range(1,len(nums)+2):
            if i not in d:
                return i


        