class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # if there are no stones return 0
        if not stones:
            return 0
        
        # if the length of the stones array is 1, return that element
        if len(stones) == 1:
            return stones[0]
        
        # min heap to max heap using negation
        heap = [-num for num in stones]

        # construct a heap using heapq's heapify
        heapq.heapify(heap)

        # while the length of the heap is greater than 1 because of length is 1
        # return that element and if length is 0 return 0
        # pop the first and second largest element from the heap
        while len(heap) > 1: 
            val1 = heapq.heappop(heap)
            val2 = heapq.heappop(heap)

            # if the differnce is zero, we destroyed both the stones
            # if the difference between them is not zero, calculate the difference
            # between the values and push the negation value of the difference
            # to the heap
            if val1 != val2:
                diffval = abs(val1 - val2)
                heapq.heappush(heap, -diffval)

        # continues until there is 0 or 1 element
        return -heap[0] if heap else 0