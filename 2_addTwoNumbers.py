# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        d1 = pre
        summ = 0 
        while l1!=None and l2!=None :
            if l1!=None:
                summ += l1.val
            if l2!=None:
                summ += l2.val
            d1.next = ListNode(summ%10)
            d1 = d1.next
            summ = int(summ/10)
            l1 = l1.next
            l2 = l2.next
        if l1!=None:
            res = l1
        elif l2!=None:
            res = l2
        else :
            res = None
        while res != None or summ!=0:
            if res != None and summ!=0:
                summ += res.val
                d1.next = ListNode(summ%10)
                d1 = d1.next
                summ = int(summ/10)
                res = res.next
            elif res!=None and summ == 0:
                d1.next = res
                break
            else:
                d1.next = ListNode(summ)
                summ = 0
        return pre.next




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