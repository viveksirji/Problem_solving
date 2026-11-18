class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d={}
        for ch in nums:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        sorted_d=sorted(d,key=d.get,reverse=True)
        return sorted_d[:k]
        

        