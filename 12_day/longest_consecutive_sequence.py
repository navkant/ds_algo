class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        A = list(sorted(set(A)))
        count = 1
        ans = 0
        for i in range(1, len(A)):
            if A[i] - 1 == A[i-1]:
                count += 1
                if i == len(A) - 1:
                    ans = max(count, ans)
            else:
                ans = max(ans, count)
                count = 1
        return ans


if __name__ == "__main__":
    obj = Solution()
    a = [97, 86, 67, 19, 107, 9, 8, 49, 23, 46, -4, 22, 72, 4, 57, 111, 20, 52, 99, 2, 113, 81, 7, 5, 21, 0, 47, 54, 76, 117, -2, 102, 34, 12, 103, 69, 36, 51, 105, -3, 33, 91, 37, 11, 48, 106, 109, 45, 58, 77, 104, 60, 75, 90, 3, 62, 16, 119, 85, 63, 87, 43, 74, 13, 95, 94, 56, 28, 55, 66, 92, 79, 27, 42, 70]
    print(obj.longestConsecutive(a))
