class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        original_bits = []

        for i in range(32):
            if A & 1:
                original_bits.append(1)
            else:
                original_bits.append(0)
            A = A >> 1

        result = 0
        for i in range(31, -1, -1):
            result = result + original_bits[31-i] * (2**i)
        return result


if __name__ == "__main__":
    a = 3
    obj = Solution()
    print(obj.reverse(a))
