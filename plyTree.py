

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
    def queue_bf(self):
        if self.root == None:
            return None
        myQueue = [self.root,]
        while myQueue!=[]:
            node = myQueue[0]
            if node.left!=None:
                myQueue.append(node.left)
            if node.right!=None:
                myQueue.append(node.right)
            print(node.val)
            myQueue.pop(0)
    def recursive_front(self,node=0):
        if node == 0:
            node = self.root
        elif node == None:
            return None
        print(node.val)
        self.recursive_front(node.left)
        self.recursive_front(node.right)
    def recursive_middle(self,node=0):
        if node == 0:
            node = self.root
        elif node == None:
            return None
        self.recursive_middle(node.left)
        print(node.val)
        self.recursive_middle(node.right)
    def recursive_back(self,node=0):
        if node == 0:
            node = self.root
        elif node == None:
            return None
        self.recursive_back(node.left)
        self.recursive_back(node.right)
        print(node.val)
    def stack_front(self):
        if self.root == None:
            return None
        node = self.root
        myStack = []
        while node!=None or myStack!=None:
            while node!=None:
                myStack.append(node)
                print(node.val)
                node = node.left
            node = myStack.pop()
            node = node.right
    def stack_middle(self):
        if self.root == None:
            return
        node = self.root
        myStack = []
        while node or myStack:
            while node:
                myStack.append(node)
                node = node.left
            node = myStack.pop()
            print(node.val)
            node = node.right
    def stack_back(self):
        if self.root == None:
            return
        node = self.root
        myStack = [node, ]
        outStack = []
        while myStack:
            node = myStack.pop()
            if node.left:
                myStack.append(node.left)
            if node.right:
                myStack.append(node.right)
            outStack.append(node)
        while outStack:
            print(outStack.pop().val)



def main():

    a = [0,1,2,3,4,None,6,7,8,9]

    atree = Tree(a)
    btree = Tree(a)

    atree.recursive_front()



if __name__ == '__main__':
    main()

