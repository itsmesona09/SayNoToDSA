class TwoSum:
    def two_sum(self, arr, target):
        hm = {}
        for i, num in enumerate(arr):
            complement = target - num
            if complement in hm:
                return [hm[complement] + 1, i + 1]
            hm[num] = i
        return []
            
ts = TwoSum()
arr = [2, 3, 2, 15]
target = 4
print(ts.two_sum(arr, target))