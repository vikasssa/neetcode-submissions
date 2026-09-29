class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # heap = []
        # counter = Counter(nums)
        # for num, freq in counter.items():
        #     heapq.heappush(heap, (freq, num))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        
        # ans = [ num for freq, num in heap]
        # return ans
        
        buckets = [[] for _ in range(len(nums) + 1)]

        counter = Counter(nums)

        for key, value in counter.items():
            buckets[value].append(key)

        ans = []

        for bucket in range(len(buckets) - 1, 0, -1):
            for num in buckets[bucket]:
                ans.append(num)
                if len(ans) == k:
                    return ans