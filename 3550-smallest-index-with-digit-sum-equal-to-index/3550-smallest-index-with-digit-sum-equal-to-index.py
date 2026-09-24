class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            s=0
            num=nums[i]
            while num>0:
                d=num%10
                s+=d
                num//=10
            if s==i:
                return i
        else:
            return -1
        
            
        

        
        
            









            
            

       

            
                
            
    
        