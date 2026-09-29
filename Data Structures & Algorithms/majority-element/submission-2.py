class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = nums[0]
        freq = 1

        for num in nums[1:]:
            if candidate != num:
                freq -= 1
            else:
                freq += 1

            if freq == 0:
                candidate = num
                freq = 1
        
        return candidate