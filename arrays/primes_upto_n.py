from typing import List


class Solution:
    def primesUptoN(self, n: int) -> List[int]:
        numbers = [True for i in range(n + 1)]
        p = 2

        while p * p <= n:
            if numbers[p]:
                for i in range(p*p, n+1, p):
                    numbers[i] = False

            p += 1

        result = []
        for i in range(2, n+1):
            if numbers[i]:
                result.append(i)
        return result


if __name__ == "__main__":
    obj = Solution()
    n = 100
    result = obj.primesUptoN(n)
    print(f"result is {result}")