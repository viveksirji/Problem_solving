
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:

        # Step 1: Calculate absolute differences
        diff = []
        for a, b in zip(nums1, nums2):
            diff.append(abs(a - b))

        # Step 2: Combine available operations
        k = k1 + k2

        # Step 3: If all differences can become zero
        if sum(diff) <= k:
            return 0

        # Step 4: Binary search for the maximum difference level
        left = 0
        right = max(diff)

        while left < right:
            mid = (left + right) // 2

            # Operations required to bring every difference to mid
            needed = 0
            for d in diff:
                if d > mid:
                    needed += d - mid

            if needed <= k:
                right = mid
            else:
                left = mid + 1

        # Step 5: Reduce all differences to the selected level
        remaining = k

        for i in range(len(diff)):
            reduction = max(0, diff[i] - left)
            diff[i] -= reduction
            remaining -= reduction

        # Step 6: Use leftover operations on differences at the level
        for i in range(len(diff)):
            if remaining == 0:
                break

            if diff[i] == left:
                diff[i] -= 1
                remaining -= 1

        # Step 7: Calculate the minimum sum of squares
        answer = 0
        for d in diff:
            answer += d * d

        return answer