class MaxSubArr:
    def maximum_subarray(self, nums):
        # # start with the first element
        # maxsum = currsum  = nums[0]
        
        # or define a least value number
        maxsum = float('-inf')
        currsum = 0
        
        for num in nums:
            currsum = max(currsum + num, num)
            maxsum = max(maxsum, currsum)
        return maxsum

maxsub = MaxSubArr()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxsub.maximum_subarray(nums))