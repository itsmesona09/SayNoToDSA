class ProdArray:
    def product_array(self, nums):
        n = len(nums)
        ltrav = [1] * n
        rtrav = [1] * n
        
        for i in range(1, len(nums)):
            ltrav[i] = ltrav[i-1] * nums[i-1]
            
        for i in range(len(nums) -2, -1, -1):
            rtrav[i] = rtrav[i+1] * nums[i+1]
            
        arr = []
        for i in range(n):
            arr.append(ltrav[i] * rtrav[i])
        return arr
        
prodarr = ProdArray()
nums = [1, 2, 3, 4]
print(prodarr.product_array(nums))