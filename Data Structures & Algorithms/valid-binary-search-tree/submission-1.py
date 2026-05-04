# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
    
        def helper(node: Optional[TreeNode], minValue: int, maxValue: int) -> bool:
            if not node:
                return True
            if node.val <= minValue or maxValue <= node.val:
                return False
            
            return helper(node.left, minValue, node.val) and helper(node.right, node.val, maxValue)
        
        return helper(root, -1001, 1001)