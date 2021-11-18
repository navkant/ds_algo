class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        count = 0
        while A != 0:
            rem = A % 2
            count = count + rem
            A = A // 2
        return count


if __name__ == "__main__":
    a = 20
    obj = Solution()
    print(obj.numSetBits(a))
