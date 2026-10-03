class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:


        time = 0

        queue = deque() # available_time, freq

        freqs = Counter(tasks)

        maxheap = [-freq for  freq in freqs.values() ]

        heapq.heapify(maxheap) #freq


        while maxheap or queue:

            time += 1

            while queue and queue[0][0] <= time:
                time, freq = queue.popleft()
                heapq.heappush(maxheap, freq)
            

            if maxheap:
                freq = heapq.heappop(maxheap)

                freq += 1

                if freq != 0:
                    queue.append((time + n + 1, freq))
        
        return time




        