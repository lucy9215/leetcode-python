# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
    ip = p
    iq = q
    path = []

    while self.isSameNode(ip,iq):
        
            

    def isSameNode(self, a, b):
        if a==b==None:
            return True
        elif a!=None and b!=None:
            if a.val==b.val and a.left==b.left and a.right==b.right:
                return True
        else:
            return False


