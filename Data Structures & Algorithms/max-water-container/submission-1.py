'''
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
'''
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water=0
        n=len(heights)
        left=0
        right=n-1
        while left<right:
            width=right-left
            current_height = min(heights[left], heights[right])
            area = width * current_height
            max_water = max(max_water, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
                
        return max_water

