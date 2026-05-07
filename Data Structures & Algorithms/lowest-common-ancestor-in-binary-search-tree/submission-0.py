# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.path=[]
        self.paths=[]
        self.helper(root,p)
        self.helper(root,q)
        ans=None
        for i in range(min(len(self.paths[0]),len(self.paths[1]))):
            if self.paths[0][i].val==self.paths[1][i].val:
                ans = self.paths[0][i]
            else:
                return ans
        return ans

    def helper(self,root,val):
        if not root:
            return False
        self.path.append(root)
        if root.val==val.val:
            self.paths.append(self.path.copy())
            self.path.pop()
            return True
        if self.helper(root.left,val) or self.helper(root.right,val):
            self.path.pop()
            return True
        self.path.pop()
        

        