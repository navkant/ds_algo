class Solution:
    """Remove duplicates in a sorted array in-place"""
    def removeDuplicates(self, nums):
        i = 1
        for j in range(1, len(nums)-1):
            if nums[j] != nums[j-1]:
                nums[i] = nums[j]
                i += 1
        print(nums)
        return i


if __name__ == "__main__":
    obj = Solution()
    a = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3]
    print(obj.removeDuplicates(a))
