# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ref = set([])
        ind = head
        while ind :
            if ind in ref:
                return True
            ref.add(ind)
            ind = ind.next
        return False 