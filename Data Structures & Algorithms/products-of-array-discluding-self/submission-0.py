class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left , right = 1, 1
        ans = []

        for num in nums:
            ans.append(left)
            left *= num

        for i in range(len(nums) - 1, -1, -1):
            ans[i] = ans[i] * right
            right = right * nums[i]
        
        return ans

   

        