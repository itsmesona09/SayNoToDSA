class TopFreq:
    def top_freq(self, nums, k):
        hm = {}
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
        
        sortedhm = sorted(hm.items(), key = lambda x: x[1], reverse = True)
        
        arr = []
        for key, value in sortedhm:
            arr.append(key)
            if len(arr) == k:
                return arr
        
        
topfreq = TopFreq()
print(topfreq.top_freq([1,1,1,2,2,3], 2))