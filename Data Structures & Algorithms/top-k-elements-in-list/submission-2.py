class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        heap = []
        counter = Counter(nums)
        for num, freq in counter.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        ans = [ num for freq, num in heap]
        return ans
        