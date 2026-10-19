# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         res = []

#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums)):
#                 for k in range(j + 1, len(nums)):
#                     s = nums[i] + nums[j] + nums[k]

#                     if s == 0:
#                         triplet = sorted([nums[i], nums[j], nums[k]])

#                         if triplet not in res:
#                             res.append(triplet)

#         return res

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums=sorted(nums)
        res=[]
        for i in range(len(nums)-2):
            if  i>0 and nums[i]==nums[i-1]:
                continue
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total==0:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while left<right and nums[left]==nums[left-1]:
                        left+=1
                    while left<right and nums[right]==nums[right+1]:
                        right-=1
                elif total<0:
                    left+=1
                else:
                    right-=1          

        return res
        

        