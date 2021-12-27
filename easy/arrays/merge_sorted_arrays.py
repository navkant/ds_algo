from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        final_array = []
        i = 0
        j = 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                final_array.append(nums1[i])
                i += 1
            else:
                final_array.append(nums2[j])
                j += 1

        while i < m:
            final_array.append(nums1[i])
            i += 1

        while j < n:
            final_array.append(nums2[j])
            j += 1

        nums1 = final_array
        print(nums1)


if __name__ == "__main__":
    obj = Solution()
    a1 = [1,2,3,0,0,0]
    x = 3
    a2 = [2,5,6]
    y = 3
    obj.merge(a1, x, a2, y)

