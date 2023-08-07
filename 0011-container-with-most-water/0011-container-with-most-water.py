class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxArea =0
        while l < r:
            currArea = min(height[l], height[r])*(r-l)
            maxArea = max(currArea, maxArea)

            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return maxArea            