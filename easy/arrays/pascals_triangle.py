from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        result = [[1], [1, 1]]

        for i in range(3, numRows+1):
            row = list()
            row.append(1)
            for j in range(1, i-1):
                val = result[i-2][j-1] + result[i-2][j]
                row.append(val)
            row.append(1)
            result.append(row)
        return result


if __name__ == "__main__":
    obj = Solution()
    n = 2
    print(obj.generate(n))