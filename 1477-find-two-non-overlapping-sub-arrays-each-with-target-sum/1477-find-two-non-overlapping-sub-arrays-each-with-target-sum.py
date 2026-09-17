class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:

        n = len(arr)
        INF = n + 1

        # best[i] = shortest target-sum subarray
        # found in arr[0 : i]
        best = [INF] * (n + 1)

        left = 0
        current_sum = 0
        answer = INF

        for right in range(n):

            current_sum += arr[right]

            # Shrink window
            while current_sum > target:
                current_sum -= arr[left]
                left += 1

            # Carry forward the previous best
            best[right + 1] = best[right]

            # Found a subarray with sum = target
            if current_sum == target:

                length = right - left + 1

                # best[left] contains a subarray
                # completely before current window
                if best[left] != INF:
                    answer = min(
                        answer,
                        best[left] + length
                    )

                # Store current subarray if it is shorter
                best[right + 1] = min(
                    best[right + 1],
                    length
                )

        if answer == INF:
            return -1

        return answer