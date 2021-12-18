class TwoSum:
    def solve(self, arr, target):
        sum_dict = {}
        result = []
        for i in range(len(array)):
            if target - arr[i] not in sum_dict:
                if arr[i] not in sum_dict:
                    sum_dict[arr[i]] = i
                else:
                    pass
            else:

                result.append(sum_dict[target - arr[i]] + 1)
                result.append(i+1)
                break
        return result


if __name__ == "__main__":
    array = [4, 7, -4, 2, 2, 2, 3, -5, -3, 9, -4, 9, -7, 7, -1, 9, 9, 4, 1, -4, -2, 3, -3, -5, 4, -7, 7, 9, -4, 4, -8 ]
    t = -3
    obj = TwoSum()
    print(obj.solve(array, t))
