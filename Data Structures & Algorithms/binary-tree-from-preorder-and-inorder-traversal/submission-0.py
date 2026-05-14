# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorderIndexMap = {}
        self.i = 0

        for i, num in enumerate(inorder):
            inorderIndexMap[num] = i

        def build(preorder, start, end):
            if start > end:
                return None
            
            index = inorderIndexMap[preorder[self.i]]
            node = TreeNode(preorder[self.i])
            self.i += 1

            node.left = build(preorder, start, index - 1)
            node.right = build(preorder, index +1, end)

            return node
        
        return build(preorder, 0, len(preorder)-1)