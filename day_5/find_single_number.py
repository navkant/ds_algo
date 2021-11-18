class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ans = 0
        for i in range(len(A)):
            ans = ans ^ A[i]
        return ans


if __name__ == "__main__":
    obj = Solution()
    arr = [1, 2, 2, 3, 1]
    print(obj.singleNumber(arr))
