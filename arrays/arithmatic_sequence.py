import sys
from typing import List, Optional

class Solution:
    def find_min_given_min(self, arr: List[int], given_min: Optional[int]) -> int:
        minimum = sys.maxsize
        for i in range(len(arr)):
            if given_min and arr[i] == given_min:
                continue
            minimum = min(arr[i], minimum)
        return minimum
            
    def isArithmeticSequence(self, arr: List[int]) -> bool:
        # add your logic here
        first_minimum = self.find_min_given_min(arr, sys.maxsize)
        second_minimum = self.find_min_given_min(arr, first_minimum)
        
        diff = second_minimum - first_minimum
        
        if diff != 1:
            for i in range(len(arr)):
                if (arr[i] - first_minimum) % diff:
                    return False
        else:
            for i in range(len(arr)):
                if (arr[i] - first_minimum) != 1:
                    return False
        
        return True

        


if __name__ == "__main__":
    obj = Solution()
    a = [4, 1, 2]
    result = obj.isArithmeticSequence(a)
    print(f"Series is AP {result}")
