class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        i = 0
        j = 0
        summ = A[0]
        while i < len(A) and j < len(A):
            print(f"i: {i} j: {j} summ: {summ}")
            if summ == B:
                return A[i:j+1]
            elif summ < B:
                j += 1
                if j == len(A):
                    break
                summ += A[j]
            elif summ >= B:
                summ -= A[i]
                i += 1
                if summ == B:
                #     import pdb
                #     pdb.set_trace()
                    return A[i:j + 1]

        return -1


if __name__ == "__main__":
    obj = Solution()
    a = [5, 10, 20, 100, 105]
    b = 110
    print(obj.solve(a, b))
