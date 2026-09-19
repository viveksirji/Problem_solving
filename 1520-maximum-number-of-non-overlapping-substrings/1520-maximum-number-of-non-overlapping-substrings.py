class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first={}
        last={}
        for i, ch in enumerate(s):
            if ch not in first:
                first[ch]=i
            last[ch]=i
        interval=[]
        for ch in first:
            start=first[ch]
            end=last[ch]
            i=start
            valid=True
            while i<=end:
                if first[s[i]]<start:
                    valid=False
                    break
                end=max(end,last[s[i]])
                i+=1
            if valid:
                interval.append((start,end))
        interval.sort(key=lambda x:x[1])
        result=[]
        prev_end=-1
        for start, end in interval:
            if start>prev_end:
                result.append(s[start:end+1])
                prev_end=end
        return result

    




        

       

               

       