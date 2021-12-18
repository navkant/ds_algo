class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        for i in range(1, len(A)):
            A[i] += A[i-1]

        sum_dict = {}
        for i in range(len(A)):
            if A[i] not in sum_dict and A[i] != 0:
                sum_dict[A[i]] = i
            else:
                return 1
        return 0


if __name__ == "__main__":
    obj = Solution()
    a = [1, -1]
    print(obj.solve(a))
