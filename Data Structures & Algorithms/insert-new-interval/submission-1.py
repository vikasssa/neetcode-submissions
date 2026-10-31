class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        ans = []

        for interval in intervals:
            #newInterval finished before current interval
            if newInterval[1] < interval[0]: 
                ans.append(newInterval)
                newInterval = interval
            #newInterval finished after current interval    
            elif newInterval[0] > interval[1]:
                ans.append(interval)
            else:
                #newInterval is overlapping with current interval
                start = min(interval[0], newInterval[0])
                end = max(interval[1], newInterval[1])
                newInterval = [start, end]
                
        ans.append(newInterval)
        return ans
        