class TwoSum:
    def twosum(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            sumval = nums[left] + nums[right]
            if sumval == target:
                return [left, right]
            elif sumval < target:
                left += 1
            else:
                right -= 1
        return [-1, -1]

sumcal = TwoSum()
nums = [2, 7, 11, 15]
target = 9
print(sumcal.twosum(nums, target))