from typing import List

class Solution:
    def pascalTriangleRow(self, rowNo: int) -> List[int]:
        # add your logic here
        triangle = [[1], [1, 1]]

        if rowNo == 1:
            return triangle[0]
        if rowNo == 2:
            return triangle[1]

        for i in range(3, rowNo + 1):
            row = [1]
            for j in range(1, len(triangle[-1])):
                row.append(triangle[-1][j - 1] + triangle[-1][j])
            row.append(1)
            triangle.append(row)

        return triangle[-1]


if __name__ == "__main__":
    obj = Solution()
    result = obj.pascalTriangleRow(6)
    print(f"result is {result}")
