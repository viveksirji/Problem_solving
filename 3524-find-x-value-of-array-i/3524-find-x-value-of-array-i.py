class Solution:
    def resultArray(self, nums: list[int], k: int) -> list[int]:
        
        # answer[r] = number of subarrays
        # whose product % k == r
        answer = [0] * k
        
        # dp[r] = number of subarrays ending
        # at previous index with product % k == r
        dp = [0] * k
        
        for num in nums:
            
            # New subarrays ending at current index
            current = [0] * k
            
            # Start a new subarray with only num
            remainder = num % k
            current[remainder] += 1
            
            # Extend all previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_remainder = (r * num) % k
                    current[new_remainder] += dp[r]
            
            # Add current subarrays to final answer
            for r in range(k):
                answer[r] += current[r]
            
            # Current becomes previous for next iteration
            dp = current
        
        return answer