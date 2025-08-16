from typing import List

class BinarySearch:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                # move low to the next position of mid
                low = mid + 1
            else:
                # move high to the prev position of mid
                high = mid - 1
        return -1
    
binarysearch = BinarySearch()
nums = [-1, 0, 3, 5, 9, 12]
target = 9
print(binarysearch.search(nums, target))