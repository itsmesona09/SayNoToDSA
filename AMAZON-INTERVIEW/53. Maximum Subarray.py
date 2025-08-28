class MaxSubArray:
    def max_sub(self, arr):
        currsum = maxsum = float('-inf')
        for num in arr:
            currsum = max(currsum + num, num)
            maxsum = max(currsum, maxsum)
        return maxsum
        
sub_arr = MaxSubArray()
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("The maximum sum is : ", sub_arr.max_sub(nums))