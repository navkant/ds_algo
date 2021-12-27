from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry_over = 0
        n = len(digits)

        for i in range(n-1, -1, -1):
            if i == n-1:
                val = digits[i] + 1 + carry_over
            else:
                val = digits[i] + carry_over
            if val >= 10:
                carry_over = 1
                digits[i] = val % 10
            else:
                carry_over = 0
                digits[i] = val
        if carry_over:
            digits.insert(0, carry_over)

        return digits


if __name__ == "__main__":
    obj = Solution()
    a = [9, 9]
    print(obj.plusOne(a))
