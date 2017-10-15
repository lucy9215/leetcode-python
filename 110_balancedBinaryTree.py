# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.diff = -1
        def dep(node):
            if node:
                dl = dep(node.left)
                dr = dep(node.right)
                diff = abs(dl-dr)
                if diff>self.diff:
                    self.diff = diff
                d = 1 + max(dl, dr)
            else:
                d = 0
            return d 
        d = dep(root)
        if 0<=self.diff<=1 or d==0:
            return True
        else :
            return False