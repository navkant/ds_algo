class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        main_string = ''.join(sorted(a))
        len_A = len(A)
        count = 0
        for i in range(len(B)):
            anagram = ''.join(sorted(B[i:i+len_A]))
            if anagram == main_string:
                count += 1
            else:
                pass
        return count


if __name__ == "__main__":
    a = 'abc'
    b = 'abcbacabc'
    obj = Solution()
    print(obj.solve(a, b))
