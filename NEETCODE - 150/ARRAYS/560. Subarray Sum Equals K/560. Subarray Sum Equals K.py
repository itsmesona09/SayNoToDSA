class SubArray:
    def subarray_sum(self, nums, k):
        hm = {0:1}
        sumval = count = 0
        for num in nums:
            sumval += num
            
            if sumval - k in hm:
                count += hm[sumval - k]
                
            hm[sumval] = hm.get(sumval, 0) + 1
            
        return count
        
subarray = SubArray()
nums = [1,2,1,2,1]
k = 3
print(subarray.subarray_sum(nums, k))