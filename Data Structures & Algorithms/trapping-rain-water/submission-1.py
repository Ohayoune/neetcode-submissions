class Solution:
    def trap(self, height: List[int]) -> int:
        res = 0
        l = 0
        maxL = 0
        maxR=0
        r = len(height)-1
        
        while l < r-1:
            maxL = max(height[l],maxL)
            maxR = max(height[r],maxR)
            if height[l] < height[r]:
        
                res += max(0,min(maxL,maxR)-height[l+1])

                l+=1
            else:
                res +=  max(0,min(maxL,maxR)-height[r-1])
                r-=1

        return res
