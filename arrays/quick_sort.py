from typing import List


class Solution:
    def partition(self, arr: List[int], low: int, high: int) -> int:
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            while i < j and arr[i] <= pivot:
                i += 1
            
            while arr[j] > pivot:
                j -= 1
            
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[low], arr[j] = arr[j], arr[low]
        return j
    
    def quick_sort(self, arr, l, h):
        if l < h:
            j = self.partition(arr, l, h)
            self.quick_sort(arr, l, j-1)
            self.quick_sort(arr, j+1, h)

    def quickSort(self, arr: List[int]) -> List[int]:
        self.quick_sort(arr, 0, len(arr)-1)


if __name__ == "__main__":
    obj = Solution()
    arr = [1, 1, 1, 1, 1, 1, 1]
    
    print(f"Initial array is {arr}")
    partition = obj.quickSort(arr)
    print(f"partition is {arr}")