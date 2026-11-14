class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in d:
                return [d[rem],i]
            else:
                d[nums[i]]=i
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]

      
       
      
        

        