# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        ll = self.sumOfLeftLeaves(root.right)

        if root.left:
            if root.left.left == root.left.right:
                ll += root.left.val
            else:
                ll += self.sumOfLeftLeaves(root.left)
                
        return ll