class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        def timetaken(rate):
            total = 0

            for num in piles:
                total += math.ceil(num/rate)
            return total

        while left <= right:
            mid = (left + right) // 2

            total_time = timetaken(mid)

            if total_time > h:
                left = mid + 1
            else:
                right = mid - 1

        return left

        