class Solution:
    def trap(self, height: List[int]) -> int:
        lmax, rmax = float('-inf'), float('-inf')
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            lmax = max(lmax, height[left])
            rmax = max(rmax, height[right])

            if lmax < rmax:
                ans += (lmax - height[left])
                left += 1
            else:
                ans += (rmax - height[right])
                right -= 1
        return ans