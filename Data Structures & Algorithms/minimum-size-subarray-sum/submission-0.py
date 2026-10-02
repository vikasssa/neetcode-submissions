class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minL = float('inf')
        left = 0
        currS = 0
        for right in range(len(nums)):
            currS += nums[right]
            while currS >= target:
                minL = min(minL, right - left + 1)
                currS -= nums[left]
                left += 1
        return 0 if minL == float('inf') else minL
        