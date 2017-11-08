# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node.next == None:
            return
        else:
            node.val = node.next.val
            node.next = node.next.next


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

    # printLinkedList(l1)
    # p = l1
    # while p:
    #     print(p)
    #     p=p.next
    # print()

    p = l1.next
    solution.deleteNode(p)

    print ('Output:', strLinkedList(l1))


if __name__ == '__main__':
    main()