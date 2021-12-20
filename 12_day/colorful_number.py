class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A: int):
        if A == 1:
            return 1
        string_number = str(A)
        n = len(string_number)
        hash_map = {}

        for i in range(1, n+1):
            for j in range(n-i+1):
                number = string_number[j:j+i]
                if int(number) == 1:
                    return 0
                product = 1
                for digit in number:
                    product *= int(digit)
                print(f"{number}: {product}")
                if product not in hash_map:
                    hash_map[product] = 1
                else:
                    return 0
        return 1


if __name__ == "__main__":
    obj = Solution()
    a = 1
    print(obj.colorful(a))
