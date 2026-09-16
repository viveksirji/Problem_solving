class Solution:
    def numberOfSets(self, n: int, k: int) -> int:

        MOD = 10**9 + 7

        N = n + k - 1
        R = 2 * k

        result = 1

        for i in range(1, R + 1):
            result = result * (N - i + 1) // i

        return result % MOD











# from math import comb

# class Solution:
#      def numberOfSets(self, n: int, k: int) -> int:

#          return comb(n + k - 1, 2 * k) % (10**9 + 7)