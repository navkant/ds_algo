class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        array_a_dict = dict()
        array_b_dict = dict()
        for i in A:
            if i not in array_a_dict:
                array_a_dict[i] = 1
            else:
                array_a_dict[i] += 1
        for i in B:
            if i not in array_b_dict:
                array_b_dict[i] = 1
            else:
                array_b_dict[i] += 1

        result = list()
        for i in A:
            if i in array_a_dict and i in array_b_dict:
                for j in range(min(array_a_dict[i], array_b_dict[i])):
                    result.append(i)
                array_b_dict.pop(i)
                array_a_dict.pop(i)
            else:
                pass
        return result


if __name__ == "__main__":
    a = [1, 2, 2, 1]
    b = [2, 3, 1, 2]
    obj = Solution()
    print(obj.solve(a, b))
