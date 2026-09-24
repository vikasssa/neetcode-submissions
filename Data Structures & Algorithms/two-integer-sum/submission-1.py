class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}

        for idx, num in enumerate(nums):
            if target - num in lookup:
                return [lookup[target-num], idx]
            if num not in lookup:
                lookup[num] = idx
        

        