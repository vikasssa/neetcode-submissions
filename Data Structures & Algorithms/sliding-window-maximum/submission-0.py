class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        left = 0
        ans = []

        for right in range(len(nums)):
            while queue and nums[right] >= nums[queue[-1]]:
                queue.pop()

            queue.append(right)

            while right - left + 1 > k:
                if queue[0] <= left:
                    queue.popleft()
                left += 1
            
            if right - left + 1 == k:
                ans.append(nums[queue[0]])
        
        return ans
            

