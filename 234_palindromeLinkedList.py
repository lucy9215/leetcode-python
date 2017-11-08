# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ref = []
        while head:
            ref.append(head)
            head = head.next
        l = len(ref)
        s = 0 
        e = l - 1
        while s<l:
            if ref[s].val != ref[e].val:
                return False
            s+=1
            e-=1
        return True
