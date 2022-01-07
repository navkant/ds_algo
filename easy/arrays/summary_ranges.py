from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        subarray = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                subarray.append(nums[i])
            else:
                result.append(subarray)
                subarray = [nums[i]]
        print(result)


if __name__ == "__main__":
    obj = Solution()
    a = [0, 2, 3, 4, 6, 8, 9]
    obj.summaryRanges(a)
