
# LeetCode 160: Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:

        pA = headA
        pB = headB

        # Each pointer traverses both lists.
        # They will meet at the intersection node or None.

        while pA != pB:

            if pA:
                pA = pA.next
            else:
                pA = headB

            if pB:
                pB = pB.next
            else:
                pB = headA

        return pB
