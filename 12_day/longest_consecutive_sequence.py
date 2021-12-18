class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        hash_map = dict()
        count = 0
        ans = 0
        for i in range(len(A)):
            number = A[i]
            if number - 1 in hash_map:
                count += 1


if __name__ == "__main__":
    obj = Solution()
    a = [2, 1]

    print(obj.longestConsecutive(a))