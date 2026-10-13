
class Solution:
    def maxAlternatingSum(self, nums: list[int]) -> int:
        nums.sort(key=lambda x: x * x)

        n = len(nums)
        mid = n // 2

        small = 0
        large = 0

        for i in range(mid):
            small += nums[i] * nums[i]

        for i in range(mid, n):
            large += nums[i] * nums[i]

        return large - small
