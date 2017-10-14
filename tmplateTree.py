



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

    a = [1]
    b = [1]

    atree = Tree(a)
    btree = Tree(a)

    aroot = atree.root
    broot = btree.root


    print ('Output:', solution.isSameTree(aroot,broot))


if __name__ == '__main__':
    main()


