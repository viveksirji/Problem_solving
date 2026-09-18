class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:

        # Store first and last occurrence of each character
        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        # Find the smallest valid interval for each character
        for ch in first:

            start = first[ch]
            end = last[ch]

            i = start
            valid = True

            while i <= end:

                # This character started before our interval
                if first[s[i]] < start:
                    valid = False
                    break

                # Expand interval if this character
                # occurs later
                end = max(end, last[s[i]])

                i += 1

            if valid:
                intervals.append((start, end))

        # Sort by ending position
        intervals.sort(key=lambda x: x[1])

        result = []
        prev_end = -1

        # Greedily select non-overlapping intervals
        for start, end in intervals:

            if start > prev_end:
                result.append(s[start:end + 1])
                prev_end = end

        return result