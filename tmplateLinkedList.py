

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
    n2 = [5]

    l1 = linkedList(n1)
    l2 = linkedList(n2)

    # printLinkedList(l1)

    print ('Output:', strLinkedList(solution.addTwoNumbers(l1, l2)))


if __name__ == '__main__':
    main()