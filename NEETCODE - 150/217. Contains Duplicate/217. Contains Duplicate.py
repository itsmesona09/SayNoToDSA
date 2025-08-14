class Duplicate:
    def contains_duplicate(self, nums):
        hm = {}
        for num in nums:
            if num in hm:
                return True
            else:
                # hm[num] = 1
                hm[num] = hm.get(num, 0) + 1
        return False

duplicate = Duplicate()
nums = [1, 2, 3, 1]
# nums = [1, 2, 3]
print(duplicate.contains_duplicate(nums))