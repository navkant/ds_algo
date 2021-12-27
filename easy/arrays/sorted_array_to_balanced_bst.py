from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        pass


if __name__ == "__main__":
    obj = Solution()
    a = [1, 2, 4, 5, 7, 8]
    obj.sortedArrayToBST(a)
