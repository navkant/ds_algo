from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def create_tree(self, array: List[int], start: int, end: int) -> TreeNode:
        print(f"start: {start} end: {end}")
        if start + 1 == end:
            parent = TreeNode(array[end])
            child = TreeNode(array[start])
            parent.left = child
            return parent
        elif start != end:
            mid = start + ((end - start) // 2)
            new_node = TreeNode(val=array[mid])
            left_child = self.create_tree(array, start, mid - 1)
            right_child = self.create_tree(array, mid+1, end)
            new_node.left = left_child
            new_node.right = right_child
            return new_node
        else:
            node = TreeNode(array[start])
            return node

    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return self.create_tree(nums, 0, len(nums)-1)


if __name__ == "__main__":
    obj = Solution()
    a = [-10,-3,0,5,9]
    x = obj.sortedArrayToBST(a)
    import pdb
    pdb.set_trace()
