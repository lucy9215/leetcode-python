class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        curMin = self.getMin()
        if curMin==None or x < curMin:
            curMin = x
        self.s.append([x,curMin])
        

    def pop(self):
        """
        :rtype: void
        """
        self.s.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if len(self.s)==0:
            return None
        else :
            v = self.s[-1][0]
            return v

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.s)==0:
            return None
        else:
            v = self.s[-1][1]
        return v
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()