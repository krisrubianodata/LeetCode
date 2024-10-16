"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        def depthfirstsearch(node):
            if not node:
                return 0
            
            res = 0

            for child in node.children:
                res = max(res, depthfirstsearch(child))

            return res + 1

        return depthfirstsearch(root)