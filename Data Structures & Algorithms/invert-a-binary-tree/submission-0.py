# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        curr = root
        if not curr.left and not curr.right:
                return curr
        else:
            leftNode = curr.left
            curr.left = self.invertTree(root.right)
            curr.right = self.invertTree(leftNode)
        return curr