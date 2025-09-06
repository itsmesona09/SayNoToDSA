class MaxProd:
    def max_prod(self, nums):
        maxprod = currprod = 1
        for i in range(len(nums)):
            currprod = max(currprod * nums[i], nums[i])
            maxprod = max(maxprod, currprod)
        return maxprod

maxprod = MaxProd()
nums = [2, 3, -2, -4]
print(maxprod.max_prod(nums))