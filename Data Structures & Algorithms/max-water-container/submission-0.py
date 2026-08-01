class Solution:
    def maxArea(self, heights: List[int]) -> int:
        s = 0
        e = len(heights)-1
        maxRain = 0
        while s < e:
            maxRain = max(min(heights[s],heights[e])*(e-s),maxRain)
            if heights[s] < heights[e]:
                s+=1
            else:
                e-=1
        
        return maxRain