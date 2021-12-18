class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        hash_map = dict()
        n = len(A)
        result = []
        for i in range(n):
            for j in range(i+1, n):
                temp = A[i] + A[j]
                if temp not in hash_map:
                    hash_map[temp] = []
                    hash_map[temp].append(i)
                    hash_map[temp].append(j)
                else:
                    if i not in hash_map[temp] and j not in hash_map[temp] and len(hash_map[temp]) <= 2:
                        hash_map[temp].append(i)
                        hash_map[temp].append(j)
                    else:
                        pass
                    if len(hash_map[temp]) == 4:
                        if not result:
                            result = hash_map[temp]
                        else:
                            temp_result = hash_map[temp]
                            for k in range(len(result[:4])):
                                if temp_result[k] == result[k]:
                                    continue
                                elif temp_result[k] > result[k]:
                                    break
                                else:
                                    result = temp_result

        return result


if __name__ == "__main__":
    a = [9, 5, 4, 9, 3, 6, 8, 7, 1, 2, 8, 7, 2, 9, 7, 1, 3, 9, 7, 8, 1, 0, 5, 5]
    obj = Solution()
    print(obj.equal(a))