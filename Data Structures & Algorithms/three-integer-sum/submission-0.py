class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        nums.sort()
        i = 0
        m = len(nums)
        while i < m:
            target = -nums[i]
            j = i + 1
            k = m - 1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    ans.add(tuple((nums[i], nums[j], nums[k])))
                    j += 1
                    k -= 1
            i += 1
        if ans:
            res = [ list(triplet) for triplet in ans]
            return res
        else:
            return []