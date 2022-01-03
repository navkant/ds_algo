from sys import maxsize
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minn = maxsize
        profit = 0

        for i in range(len(prices)):
            minn = min(minn, prices[i])
            profit = max(profit, prices[i] - minn)

        return profit


if __name__ == "__main__":
    a = [7, 1, 5, 3, 6, 4]
    obj = Solution()
    print(obj.maxProfit(a))
