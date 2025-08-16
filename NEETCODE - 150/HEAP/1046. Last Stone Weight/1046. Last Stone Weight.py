import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        
        heap = [-num for num in stones]
        heapq.heapify(heap)
        while len(heap) > 1: 
            val1 = heapq.heappop(heap)
            val2 = heapq.heappop(heap)
            
            if val1 != val2:
                diffval = abs(val1 - val2)
                heapq.heappush(heap, -diffval)

        return -heap[0] if heap else 0