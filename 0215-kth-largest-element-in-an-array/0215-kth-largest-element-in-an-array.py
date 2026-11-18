class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        # for i in range(k-1):
        #     maximum=max(nums)
        #     nums.remove(maximum)
        # return max(nums)
        nums.sort()
        return nums[len(nums)-k]
        