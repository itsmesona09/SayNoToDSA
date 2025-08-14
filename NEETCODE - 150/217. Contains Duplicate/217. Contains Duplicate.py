class Duplicate:
    def contains_duplicate(self, nums):
        hm = {}
        for num in nums:
            if num in hm:
                return True
            else:
                hm[num] = hm.get(nums[num], 0) + 1
        return False

duplicate = Duplicate()
nums = [1, 2, 3, 1]
print(duplicate.contains_duplicate(nums))