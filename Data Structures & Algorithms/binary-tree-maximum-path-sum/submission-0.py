# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = [-math.inf]

        def maxhelper(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            left = maxhelper(node.left)
            right = maxhelper(node.right)
            result[0] = max(result[0], left + right + node.val)
            result[0] = max(result[0], left + node.val)
            result[0] = max(result[0], node.val + right)
            result[0] = max(result[0], node.val)

            return max(node.val, max(left + node.val, node.val + right))
        
        
        maxhelper(root)
        return result[0]