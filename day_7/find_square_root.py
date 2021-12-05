class Solution:
    def find_square_root(self, number):
        """finds square root of given number"""
        for i in range((number//2)+1):
            if i * i > number:
                return i-1
            elif i * i == number:
                return i


if __name__ == "__main__":
    n = 3
    obj = Solution()
    print(obj.find_square_root(n))