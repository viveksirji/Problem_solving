class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            s = sum(map(int, str(nums[i])))
            if s == i:
                return i
        return -1