from typing import List


class Solution:
    def merge(self, arr1, arr2):
        i = 0
        j = 0
        result = []
        while i < len(arr1) and j < len(arr2):
            if arr1[i] <= arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1

        if i < len(arr1):
            while i < len(arr1):
                result.append(arr1[i])
                i += 1

        if j < len(arr2):
            while j < len(arr2):
                result.append(arr2[j])
                j += 1
        return result

    def sort(self, arr, start, end):
        if end - start == 0:
            print(f"start: {start} end: {end}")
            return [arr[start]]

        mid = start + (end - start) // 2
        print(f"start: {start} mid: {mid} end: {end}")
        part_1 = self.sort(arr, start, mid)
        part_2 = self.sort(arr, mid+1, end)
        x = self.merge(part_1, part_2)
        print(f"returning {x}")
        return x

    def mergeSort(self, arr: List[int]) -> List[int]:
        # add your logic here
        return self.sort(arr, 0, len(arr) - 1)


if __name__ == "__main__":
    obj = Solution()
    a = [5, 4, 2, 5, 3, 1]
    result = obj.mergeSort(a)
    print("sorted array is: ", result)

