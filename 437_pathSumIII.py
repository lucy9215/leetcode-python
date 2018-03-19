# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumFromRoot(self, root, sum):
        if not root:
            return 0 

        count = (root.val == sum) + self.sumFromRoot(root.left, sum - root.val) + self.sumFromRoot(root.right, sum - root.val)
        
        return count

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """

        if not root:
            return 0 
        
        count = self.sumFromRoot(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)  
        
        return count


class Solution(object):
    def pathSum(self, root, summ):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def helper(root, mapping, pSum):
            if not root :
                return 0
            pSum += root.val
            res = mapping.get(pSum-summ,0) #get number of ways that end at the current node
            mapping[pSum] = mapping.get(pSum,0) + 1 #update number of ways
            res+= helper(root.left, mapping, pSum) + helper(root.right, mapping, pSum) 
            mapping[pSum] -= 1 #update number of ways
            return res
        
        mapping = {0:1}
        res = helper(root, mapping, 0)
        return res
















