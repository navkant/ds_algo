class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        n = len(A)
        result = 0

        for i in range(n-1):
            if A[i] % 2 == 0:
                prev_even = True
            else:
                prev_even = False
            count = 1
            for j in range(i+1, n):
                if prev_even is True:
                    if A[j] % 2 != 0:
                        count += 1
                        prev_even = False
                else:
                    if A[j] % 2 == 0:
                        count += 1
                        prev_even = True

            result = max(result, count)
        return result


if __name__ == "__main__":
    a = [1, 2, 2, 5, 6]
    obj = Solution()
    print(obj.solve(a))
