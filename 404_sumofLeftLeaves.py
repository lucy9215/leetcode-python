# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0 
        if root.left and root.left.left == None and root.left.right == None:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            summ = self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
            return summ
        




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

    a = [3,9,20,0,0,15,7]

    atree = Tree(a)

    aroot = atree.root

    print ('Output:', solution.sumOfLeftLeaves(aroot))


if __name__ == '__main__':
    main()


