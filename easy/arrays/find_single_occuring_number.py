from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums)):
            result = result ^ nums[i]

        return result


if __name__ == "__main__":
    obj = Solution()
    a = [4, 1, 2, 1, 2]
    print(obj.singleNumber(a))
