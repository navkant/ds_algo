class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        print(A)
        for i in range(len(A)):
            if A[i] == 0:
                A[i] = -1

        for i in range(1, len(A)):
            A[i] += A[i-1]

        sum_dict = {}
        ans = 0
        print(A)
        for i in range(len(A)):
            if A[i] not in sum_dict and A[i] != 0:
                sum_dict[A[i]] = i
            elif A[i] == 0:
                ans = max(ans, i + 1)
            else:
                ans = max(ans, i - sum_dict[A[i]])
        return ans


if __name__ == "__main__":
    obj = Solution()
    a = [0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1]
    print(obj.solve(a))
