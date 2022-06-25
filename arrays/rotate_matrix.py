from typing import List


class Solution:
    def rotateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        hash_map = {}
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                hash_map[(j, len(matrix) - i - 1)] = matrix[i][j]

        result = []
        for i in range(len(matrix[0])):
            row = []
            for j in range(len(matrix)):
                row.append(hash_map[(i, j)])
            result.append(row)
        
        return result


if __name__ == "__main__":
    obj = Solution()
    a = [[1, 2], [3, 4], [5, 6]]

    result = obj.rotateMatrix(a)
    for row in result:
        print(row)
