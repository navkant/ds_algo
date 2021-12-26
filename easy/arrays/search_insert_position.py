from typing import List

class Solution:
    def binary_search(self, arr, start, end, key):
        while start != end:
            if start + 1 == end:
                return end

            mid = start + ((end - start) // 2)
            print(f"start: {start} mid: {mid} end: {end}")
            if arr[mid] == key:
                return mid
            elif key < arr[mid]:
                end = mid 
            else:
                start = mid


    def searchInsert(self, nums: List[int], target: int) -> int:
        if target <= nums[0]:
            return 0
        elif target > nums[len(nums) - 1]:
            return len(nums)
        return self.binary_search(nums, 0, len(nums) - 1, target)


if __name__ == "__main__":
    obj = Solution()
    a = [1, 3]
    t = 1
    print(obj.searchInsert(a, t))
