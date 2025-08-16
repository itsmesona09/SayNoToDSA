import heapq
class TopFreq:
    # def top_freq(self, nums, k):
    #     hm = {}
    #     for n in nums:
    #         hm[n] = hm.get(n, 0) + 1
        
    #     sortedhm = sorted(hm.items(), key = lambda x: x[1], reverse = True)
        
    #     arr = []
    #     for key, value in sortedhm:
    #         arr.append(key)
    #          if len(arr) == k:
    #             return arr
    
    def top_freq_heap(self, nums, k):
        hm = {}
        for i in range(len(nums)):
            hm[nums[i]] = hm.get(nums[i], 0) + 1
        print("HASHMAP:", hm)

        heap = [(-freq, num) for num ,freq in hm.items()]
        heapq.heapify(heap)
        
        print("HEAP AFTER HEAPIFY:", heap)
        
        res = []
        for _ in range(k):
            freq, num = heapq.heappop(heap)
            res.append(num)
        
        return res
        
topfreq = TopFreq()
# print(topfreq.top_freq([9,9,9,5,5,7], 2))
# res1 = topfreq.top_freq_heap([1], 1)
res2 = topfreq.top_freq_heap([9,9,9,5,5,7], 2)
# print(res1)
print(res2)