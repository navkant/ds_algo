class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        sub_dict = {}

        for i in A:
            if B - i not in sub_dict:
                sub_dict[i] = 1
            else:
                return 1


if __name__ == "__main__":
    A = [1, 2, 3, 4]
    B = 7
    obj = Solution()
    print(obj.solve(A, B))