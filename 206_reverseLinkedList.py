# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        ref = []
        p = head
        while p!=None:
            ref.append(p)
            p = p.next
        l = len(ref)-1
        for i in range(l,0,-1):
            ref[i].next = ref[i-1]
        ref[0].next = None
        p = ref[-1]
        return p
        



class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None  

def linkedList(somelist):
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

    n1 = [5,7,8,9]

    l1 = linkedList(n1)


    print ('Output:', strLinkedList(solution.reverseList(l1)))


if __name__ == '__main__':
    main()