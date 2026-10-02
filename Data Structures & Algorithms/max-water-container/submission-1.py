class Solution:
    def maxArea(self, heights: List[int]) -> int:

        maxArea = float('-inf')

        i = 0
        j = len(heights) - 1

        while i < j:
            currentArea = (j - i) * min(heights[i], heights[j])
            maxArea = max(maxArea, currentArea)

            #always skip lowest height to avoid maxArea remaining same
            if heights[i] > heights[j]:
                j -= 1
            else:
                i += 1
        return maxArea

        