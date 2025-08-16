import heapq

class KthLargest:
    def __init__(self, nums, k):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        
    def add(self, val):
        heapq.heappush(self.heap, val)
        # print(self.heap)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        
        return self.heap[0]

if __name__ == "__main__":
    kthlargest = KthLargest([4, 5, 8, 2], 3)
    print(kthlargest.add(3))
    print(kthlargest.add(10))
    print(kthlargest.add(7))