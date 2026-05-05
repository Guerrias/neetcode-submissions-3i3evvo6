# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        result = [k, -1]

        def helper(node: Optional[TreeNode]) -> None:
            if not node:
                return

            if result[0] == 0:
                return
            
            helper(node.left)
            if result[0] > 0:
                result[0] -= 1
                result[1] = node.val

            helper(node.right)
        
        helper(root)
        return result[1]
            