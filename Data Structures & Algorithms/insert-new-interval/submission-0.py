class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans = []

        for interval in intervals:
            if newInterval[1] < interval[0]:
                ans.append(newInterval)
                newInterval = interval
            elif newInterval[0] > interval[1]:
                ans.append(interval)
            else:
                start = min(interval[0], newInterval[0])
                end = max(interval[1], newInterval[1])
                newInterval = [start, end]
                
        ans.append(newInterval)
        return ans
        