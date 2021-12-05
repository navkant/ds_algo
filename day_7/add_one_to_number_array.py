class Solution:
    # @param A : list of integers
    # @return a list of integers
    def plusOne(self, A):
        n = len(A)
        carry_over = 0

        for i in range(n-1, -1, -1):
            if i == n - 1:
                A[i] = A[i] + carry_over + 1
                carry_over = 0
            else:
                A[i] = A[i] + carry_over
                carry_over = 0
            if A[i] > 9:
                A[i] = A[i] % 10
                carry_over = 1

        if carry_over:
            A.insert(0, carry_over)
        A = int(''.join([str(x) for x in A]))
        print(A)


if __name__ == "__main__":
    a = [1, 9, 9, 9, 9, 9, 9]
    obj = Solution()
    obj.plusOne(a)