class Solution:
    # @param A : list of integers
    # @return a strings
    def solve(self, A):
        number_set = set(A)
        if len(number_set) != 2:
            return "LOSE"
        else:
            return "WIN"


if __name__ == "__main__":
    obj = Solution()
    a = [1, 1, 2, 2, 3]
    print(obj.solve(a))