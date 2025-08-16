class TwoSum:
    def two_sum(self, nums, k):
        hm = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hm:
                return [hm[complement] + 1, i + 1]
            else:
                hm[nums[i]] = i
        return [-1, -1]
        
twosum = TwoSum()
nums = [2, 7, 11, 15]
target = 9
print(twosum.two_sum(nums, target))