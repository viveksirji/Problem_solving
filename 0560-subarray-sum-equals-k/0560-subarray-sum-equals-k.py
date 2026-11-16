class Solution:
    def subarraySum(self, nums, k):
        seen = {0: 1}
        count = 0

        for i in range(len(nums)):
            if i > 0:
                nums[i] += nums[i - 1]   # nums[i] now holds the prefix sum up to i

            if nums[i] - k in seen:
                count += seen[nums[i] - k]

            if nums[i] in seen:
                seen[nums[i]] += 1
            else:
                seen[nums[i]] = 1

        return count
# class Solution:
#     def subarraySum(self, nums, k):
#         count = 0

#         for start in range(len(nums)):
#             total = 0
#             for end in range(start, len(nums)):
#                 total += nums[end]
#                 if total == k:
#                     count += 1

#         return count