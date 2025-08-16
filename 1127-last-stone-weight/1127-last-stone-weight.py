class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) < 2:
            return stones[0]
        
        heap = [-num for num in stones]

        heapq.heapify(heap)

        while len(heap) > 1: 
            val1 = heapq.heappop(heap)
            val2 = heapq.heappop(heap)

            diffval = abs(val1 - val2)
            heapq.heappush(heap, -diffval)

        return -heap[0]