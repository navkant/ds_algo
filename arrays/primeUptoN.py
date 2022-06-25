from typing import List


class Solution:
    def findSquareRoot(self, number: int):
        if number <= 3:
            return 1

    def primesUptoN(self, n: int) -> List[int]:
        result = [2, 3]
        if n == 1:
            return []

        if n == 2:
            result.append(2)
            return [2]

        if n == 3:
            result.append(3)
            return [2, 3]

        for j in range(4, n+1):
            prime = True
            for k in range(2, j//2 + 1):
                if j % k:
                    pass
                else:
                    prime = False
                    break
            if prime:
                result.append(j)
            else:
                pass

        return result


if __name__ == "__main__":
    obj = Solution()
    n = 1
    result = obj.primesUptoN(n)
    print(f"result is {result}")
