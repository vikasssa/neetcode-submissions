class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def euclidean(x, y):
            return math.sqrt(x**2 + y**2)
        

        heap = []

        for x, y in points:
            dist = euclidean(x, y)
            heapq.heappush(heap, (-dist,[x,y]))

            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = [point[1] for point in heap]
        return ans