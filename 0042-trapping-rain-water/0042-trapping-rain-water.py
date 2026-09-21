class Solution:
    def trap(self, height: list[int]) -> int:
        left,right,maxleft,maxright=0,len(height)-1,0,0
        total_water=0
        while left<=right:
            if height[left]<=height[right]:
                if maxleft<height[left]:
                    maxleft=height[left]
                else:
                    total_water+=maxleft-height[left]
                left+=1
            else:
                if maxright<height[right]:
                    maxright=height[right]
                else:
                    total_water+=maxright-height[right]
                right-=1
        return total_water
         

