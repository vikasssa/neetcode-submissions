class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def dayss(capacity):
            count = 1
            curr = 0
            for weight in weights:
                curr += weight
                if curr > capacity:
                    count += 1
                    curr = weight
            return count
        

        left = max(weights)
        right = sum(weights)

        while left <= right:
            mid = (left + right) // 2

            if dayss(mid) > days:
                left = mid + 1
            else:
                right = mid - 1
        return left



        