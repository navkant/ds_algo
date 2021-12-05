from day_7.find_square_root import Solution as sqrt


class Solution:
    def isPrime(self, number):
        """returns True is number is prime else False"""
        if number in [2, 3, 5]:
            return True
        sqrt_calculator = sqrt()
        root = sqrt_calculator.find_square_root(number)
        print(number)
        for i in range(2, root+1):
            if number % i == 0:
                return False
        return True


if __name__ == "__main__":
    n = 3
    obj = Solution()
    print(obj.isPrime(n))