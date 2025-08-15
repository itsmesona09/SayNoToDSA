class TwoSum:
    def twosum(self, nums, target):
        if sorted(nums) == nums:
            left, right = 0, len(nums) - 1
            while left <= right:
                sumval = nums[left] + nums[right]
                if sumval == target:
                    return [left, right]
                elif sumval < target:
                    left += 1
                else:
                    right -= 1
        else:
            hm = {}
            for i in range(len(nums)):
                complement = target -  nums[i]
                if complement in nums:
                    return [i, nums[complement]]
                else:
                    hm[nums[i]] = i
        return [-1, -1]

sumcal = TwoSum()
nums = [2, 7, 1, 15]
target = 9
print(sumcal.twosum(nums, target))