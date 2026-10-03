class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        sorted_tasks = sorted([(enquetime, processtime, index) for index, (enquetime,processtime) in enumerate(tasks)])

        queue = deque(sorted_tasks)

        minheap = []

        ans = []

        time = 0
        while queue or minheap:
            
            if not minheap and  queue:
                time = max(time, queue[0][0])

            while queue and queue[0][0] <= time:
                etime, ptime, i = queue.popleft()
                heapq.heappush(minheap, (ptime,i))
            

            ptime, i = heapq.heappop(minheap)
            ans.append(i)
            time += ptime
        
        return ans


