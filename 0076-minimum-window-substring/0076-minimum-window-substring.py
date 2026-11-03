class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mapS = [0] * 256
        mapT = [0] * 256

        for ch in t:
            mapT[ord(ch)] += 1

        required = 0                       # distinct characters in t
        for i in range(256):
            if mapT[i] > 0:
                required += 1

        formed = 0                         # distinct characters currently satisfied
        left = 0
        min_len = float("inf")
        min_start = 0

        for right in range(len(s)):
            c = ord(s[right])
            mapS[c] += 1
            if mapT[c] > 0 and mapS[c] == mapT[c]:
                formed += 1

            while formed == required:
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_start = left

                d = ord(s[left])
                mapS[d] -= 1
                if mapT[d] > 0 and mapS[d] < mapT[d]:
                    formed -= 1
                left += 1

        if min_len == float("inf"):
            return ""
        else:
            return s[min_start:min_start + min_len]