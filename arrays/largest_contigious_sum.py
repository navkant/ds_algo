from typing import List
import sys


class Solution:
    def largestContiguousSum(self, arr: List[int]) -> int:
        result = sys.maxsize * -1
        summ = 0

        for i in range(len(arr)):
            summ += arr[i]
            result = max(summ, result)

            if summ < 0:
                summ = 0

        return result


if __name__ == "__main__":
    arr = [4, -6, 2, 5]
    obj = Solution()
    result = obj.largestContiguousSum(arr)
    print(f"max sum is {result}")
