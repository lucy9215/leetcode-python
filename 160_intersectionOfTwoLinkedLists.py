# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pa = headA
        pb = headB
        while pa is not pb:
            pa = pa.next if pa else headB
            pb = pb.next if pb else headA
        return pa


        # ref = set([])
        # while headA or headB:
        #     if headA is headB:
        #         return headA
        #     if headA in ref:
        #         return headA
        #     if headB in ref:
        #         return headB
        #     if headA:
        #         ref.add(headA)
        #         headA = headA.next
        #     if headB:
        #         ref.add(headB)
        #         headB = headB.next
        # return None
