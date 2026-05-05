# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        result = -math.inf

        def maxhelper(node) -> int:
            if not node:
                return 0
            leftMax = maxhelper(node.left)
            rightMax = maxhelper(node.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)

            nonlocal result
            result = max(result, leftMax + node.val + rightMax)

            return node.val + max(leftMax, rightMax)
        
        
        maxhelper(root)
        return result