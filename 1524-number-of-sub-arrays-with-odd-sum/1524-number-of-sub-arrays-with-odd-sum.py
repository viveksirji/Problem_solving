class Solution:
    def numOfSubarrays(self, arr: list[int]) -> int:
        MOD = 10**9 + 7
        even = 1
        odd = 0
        ans = 0
        s = 0
        for x in arr:
            s = (s + x) % 2
            if s == 1:
                ans = (ans + even) % MOD
                odd += 1
            else:
                ans = (ans + odd) % MOD
                even += 1
        return ans




# class Solution:
#     def numOfSubarrays(self, arr: list[int]) -> int:
#         count=0
#         for i in range(len(arr)):
#             for j in range(i,len(arr)):
#                 total=sum(arr[i:j+1])
#                 if total%2==1:
#                     count+=1
#         return count
