from typing import List


class Solution:
    def mergeIntervals(self, intervals: List[List[int]]) -> List[List[int]]:
        arr = sorted(intervals, key=lambda x: x[0])
        result = [arr[0]]

        for i in range(1, len(arr)):
            if arr[i][0] <= result[-1][1]:
                if arr[i][1] < result[-1][1]:
                    pass
                else:
                    result[-1][1] = arr[i][1]
            else:
                result.append(arr[i])

        return result


if __name__ == "__main__":
    obj = Solution()
    a = [[5, 6], [1, 2], [2, 3], [1, 4]]
    result = obj.mergeIntervals(a)
    print(f"result is {result}")
