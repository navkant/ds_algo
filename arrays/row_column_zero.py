from typing import List


class Solution:
    def setRowColumnZeroes(self, matrix: List[List[int]]) -> None:
        row_hash = {}
        col_hash = {}

        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    row_hash[i] = 1
                    col_hash[j] = 1
                else:
                    pass

        new_matrix = []
        for i in range(len(matrix)):
            row = []
            for j in range(len(matrix[i])):
                if i in row_hash or j in col_hash:
                    row.append(0)
                else:
                    row.append(matrix[i][j])
            new_matrix.append(row)

        breakpoint()
        # add your logic here


if __name__ == "__main__":
    obj = Solution()
    a = [[1, 1, 0], [1, 1, 1], [1, 1, 1]]
    obj.setRowColumnZeroes(a)
