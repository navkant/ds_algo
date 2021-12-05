class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        result = []
        for i in range(len(A)):
            if i == 0:
                result.append(A[i] * A[i+1])
            elif i == len(A) - 1:
                result.append(A[i-1] * A[i])
            else:
                result.append(A[i-1] * A[i+1])
        print(result)
        return result


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    obj = Solution()
    obj.solve(a)
