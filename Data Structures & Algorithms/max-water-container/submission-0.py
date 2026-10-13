class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        area = (len(heights) - 1) * min(heights[l], heights[r])
        while l < r:
            a = (r - l) * min(heights[l], heights[r])
            if (a > area):
                area = a
            
            if (heights[l] <= heights[r]):
                l += 1
            else:
                r -= 1

        return area