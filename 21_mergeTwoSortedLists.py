# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 == None and l2 == None:
            return None 
        elif l1!=None or l2!=None:
            if l1!=None and l2==None :
                return l1
            elif l2!=None and l1==None:
                return l2

        out = ListNode(0)
        ind = out 
        while l1!=None and l2!=None:
            if l1.val>l2.val:
                ind.next = l2
                l2 = l2.next
                ind = ind.next
            else :
                ind.next = l1
                l1 = l1.next
                ind = ind.next
        if l1==None:
            ind.next = l2
        else :
            ind.next = l1
        return out.next

            






class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None  

def linkedList(somelist):
    if somelist == []:
        return None
    nodes = [ListNode(i) for i in somelist]
    for i,n in enumerate(nodes[:-1]):
        nodes[i].next = nodes[i+1]
    return nodes[0]

def strLinkedList(linkedList):
    stri = ''
    while linkedList!= None :
        stri += str(linkedList.val)
        linkedList = linkedList.next
    return stri

def main():
    solution = Solution()

    n1 = [1]
    n2 = [1,2]

    l1 = linkedList(n1)
    l2 = linkedList(n2)

    # printLinkedList(l1)

    print ('Output:', strLinkedList(solution.mergeTwoLists(l1, l2)))


if __name__ == '__main__':
    main()