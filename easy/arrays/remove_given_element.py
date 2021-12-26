from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        print(nums)
        return i



if __name__ == "__main__":
    arr = [0,1,2,3,3,0,4,2]
    element = 2
    obj = Solution()
    obj.removeElement(arr, element)
