class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        len_a = len(A)
        len_b = len(B)

        if len_a > len_b:
            B = "0" * (len_a-len_b) + B
        else:
            A = "0" * (len_b-len_a) + A

        result = []
        carry_over = 0
        for i in range(len(A)-1, -1, -1):
            if int(A[i]) + int(B[i]) + carry_over == 3:
                carry_over = 1
                result.append('1')
            elif int(A[i]) + int(B[i]) + carry_over == 2:
                carry_over = 1
                result.append('0')
            elif int(A[i]) + int(B[i]) + carry_over in [0, 1]:
                result.append(str(int(A[i]) + int(B[i]) + carry_over))
                carry_over = 0

        if carry_over:
            result.append('1')
        result = result[::-1]
        return ''.join(result)

#   11
#   11
#    0


if __name__ == "__main__":
    obj = Solution()
    print('->' + obj.addBinary(
        '1010110111001101101000',
        '1000011011000000111100110'))
    print('  ' + '1001110001111010101001110')

# 0001010110111001101101000
# 1000011011000000111100110

