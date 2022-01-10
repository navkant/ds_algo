from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        i = 0
        j = 0

        while i < len(nums):
            if nums[i] == 0:
                while j < len(nums) and nums[j] == 0:
                    j += 1
                if j == len(nums):
                    break
                import pdb
                pdb.set_trace()
                nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j = i

        return nums


if __name__ == "__main__":
    obj = Solution()
    arr = [1, 0, 1]
    print(obj.moveZeroes(arr))
