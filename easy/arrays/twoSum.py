from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}
        for i in range(len(numbers)):
            if target - numbers[i] not in hash_map:
                hash_map[numbers[i]] = i
            else:
                return [hash_map[target - numbers[i]] + 1, i+1]


if __name__ == "__main__":
    obj = Solution()
    a = [2,7,11,15]
    t = 9
    print(obj.twoSum(a, t))
