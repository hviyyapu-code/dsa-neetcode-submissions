class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        max_water=0
        for i in range(n):
            for j in range(i+1, n):
                curr_height=min(heights[i], heights[j])
                width= j-i
                area=width*curr_height
                max_water=max(max_water, area)

        return max_water
        