# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        if p == None:
            return None
        while p.next!=None:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next
        return head


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

    n1 = []
    n1 = [5,5,7,8,8,9]

    l1 = linkedList(n1)

    print ('Output:', strLinkedList(solution.deleteDuplicates(l1)))


if __name__ == '__main__':
    main()