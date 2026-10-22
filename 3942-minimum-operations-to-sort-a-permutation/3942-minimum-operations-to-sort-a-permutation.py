# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         n, shift = len(nums), nums.index(0)
#         ring = lambda k: nums[(shift + k) % n]  # the circle, read from 0
#         if all(ring(k) == k for k in range(n)):  # counts up along the arrow
#             return min(shift, n - shift + 2)  # walk ahead, or turn, walk back, turn back
#         if all(ring(k) == -k % n for k in range(n)):  # counts up against the arrow
#             return min(shift + 2, n - shift)  # walk ahead and turn, or turn and walk back
#         return -1
class Solution:

    def minOperations(self, nums):

        n = len(nums)

        sortinc = True
        sortdec = True

        for i in range(n):

            if nums[i] != (nums[(i - 1 + n) % n] + 1) % n:
                sortinc = False

            if nums[i] != (nums[(i - 1 + n) % n] - 1 + n) % n:
                sortdec = False

        if sortinc:

            k = nums[0]

            a = (n - k) % n
            b = k + 2

            return min(a, b)

        if sortdec:

            k = nums[0]

            a = n - k
            b = k + 2

            return min(a, b)

        return -1