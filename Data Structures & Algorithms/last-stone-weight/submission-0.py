class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [ -n for n in stones]

        heapq.heapify(heap)


        while len(heap) > 1:

            x = - heapq.heappop(heap)

            if heap:
                y = - heapq.heappop(heap)

            if x == y:
                pass
            else:
                heapq.heappush(heap,-(x-y) ) 
        
        if heap:
            return - heap[0]
        else:
            return 0