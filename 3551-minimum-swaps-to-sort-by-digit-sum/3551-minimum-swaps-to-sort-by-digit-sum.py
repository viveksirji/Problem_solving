class Solution:
    def minSwaps(self, nums):
        def digit_sum(n):
            s = 0
            for digit in str(n):
                s += int(digit)
            return s

        def get_key(n):
            return (digit_sum(n), n)

        n = len(nums)
        sorted_nums = sorted(nums, key=get_key)

        pos = {}
        for i in range(n):
            pos[sorted_nums[i]] = i

        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i]:
                continue

            j = i
            cycle_size = 0

            while not visited[j]:
                visited[j] = True
                j = pos[nums[j]]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps