from typing import List

#  [1, 2, 3, 4, 5, 6]
#  [1, 2, 3, 4] [5, 6]
#  [4, 3, 2, 1] [6, 5]
#  [5, 6, 1, 2, 3, 4]

class ArrayRotation:
    def reverse_array(self, arr: List[int]) -> List[int]:
        n = len(arr)
        for i in range(n//2):
            arr[i], arr[n-i-1] = arr[n-i-1], arr[i]
        return arr

    def rotate_right(self, arr: List[int], shift: int) -> List[int]:
        shift = len(arr) - shift
        left_part = arr[:shift]
        right_part = arr[shift:]
        left_part = self.reverse_array(left_part)
        right_part = self.reverse_array(right_part)
        intermediate_array = left_part + right_part
        return self.reverse_array(intermediate_array)

    def rotate_left(self, arr: List[int], shift: int) -> List[int]:
        left_part = arr[:shift]
        right_part = arr[shift:]
        left_part = self.reverse_array(left_part)
        right_part = self.reverse_array(right_part)
        intermediate_array = left_part + right_part
        return self.reverse_array(intermediate_array)

    def rotate_array(self, array: List[int], shift: int, direction: str) -> List[int]:
        if direction == 'left':
            result = self.rotate_left(array, shift)
        else:
            result = self.rotate_right(array, shift)
        return result


if __name__ == "__main__":
    obj = ArrayRotation()
    a = [1, 2, 3, 4, 5, 6]
    print(f"5 to left: {obj.rotate_array(a, 5, 'left')}")
    print(f"2 to right: {obj.rotate_array(a, 2, 'right')}")
