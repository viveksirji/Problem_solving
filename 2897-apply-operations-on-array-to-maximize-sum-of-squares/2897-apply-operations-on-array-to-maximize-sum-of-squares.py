
class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        MOD = 10**9 + 7

        # Step 1: Count the set bits
        count = [0] * 31

        for num in nums:
            for bit in range(31):
                if num & (1 << bit):
                    count[bit] += 1

        # Step 2: Construct k maximum numbers
        result = 0

        for i in range(k):
            num = 0

            for bit in range(31):
                if count[bit] > 0:
                    num |= (1 << bit)
                    count[bit] -= 1

            # Step 3: Add the square
            result = (result + num * num) % MOD

        return result
