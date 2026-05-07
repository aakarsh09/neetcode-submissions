# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.ans=0
        self.count=0
        self.helper(root,k)
        return self.ans

    def helper(self,root,k):
        if not root:
            return None
        self.helper(root.left,k)
        self.count+=1
        if self.count==k:
            self.ans=root.val
            return root
        self.helper(root.right,k)




# def inorder(node):
#     if node:
#         yield from inorder(node.left)
#         yield node.val
#         yield from inorder(node.right)

# Then:

# for i, val in enumerate(inorder(root)):
#     if i == k-1:
#         return val