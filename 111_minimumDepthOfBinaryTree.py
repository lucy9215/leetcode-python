# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            dl = self.minDepth(root.left)
            dr = self.minDepth(root.right)
            minn = min(dl,dr)
            if minn !=0:
                d = 1 + minn
            else:
                d = 1 + max(dl,dr)
        else:
            d = 0
        return d
