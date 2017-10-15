# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isSymTree(p,q):
            if p and q:
                return p.val==q.val and isSymTree(p.left,q.right) and isSymTree(p.right, q.left)
            return p==q 
        if root==None:
            return True
        p = root.left
        q = root.right
        return isSymTree(p,q)




class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Tree(object):
    """breadth first contruction"""
    def __init__(self, somelist):
        if somelist==[]:
            self.root = None
            return 
        copy = somelist[:]
        self.root=TreeNode(copy.pop(0))
        myQueue = [self.root,]
        while copy!=[]:
            if myQueue[0].left == None:
                myQueue[0].left = TreeNode(copy.pop(0))
                myQueue.append(myQueue[0].left)
            elif myQueue[0].right == None:
                myQueue[0].right = TreeNode(copy.pop(0))
                myQueue.append(myQueue[0].right)
            else:
                myQueue.pop(0)


def main():
    solution = Solution()

    a = [1,2,2,None,3,3,None]

    atree = Tree(a)

    aroot = atree.root

    print ('Output:', solution.isSymmetric(aroot))


if __name__ == '__main__':
    main()

