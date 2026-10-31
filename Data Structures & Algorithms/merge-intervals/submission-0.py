class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda k : k[0])

        ans = []
        newInterval = intervals[0]
        for interval in intervals[1:]:
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


        