# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if not root:
            return []
        if root.left == None and root.right==None:
            r = str(root.val)
        else:
            r = [str(root.val) + '->' + path for child in (root.left, root.right) if child for path in self.binaryTreePaths(child)]
        return r 
        