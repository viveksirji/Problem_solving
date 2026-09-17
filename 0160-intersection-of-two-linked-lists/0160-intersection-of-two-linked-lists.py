
# LeetCode 160: Intersection of Two Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def getIntersectionNode(self, headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:

        # Store all nodes from List A in a set
        visited = set()

        curr = headA

        while curr:
            visited.add(curr)
            curr = curr.next

        # Traverse List B and check whether
        # any node is already present in the set
        curr = headB

        while curr:
            if curr in visited:
                return curr

            curr = curr.next

        # No intersection found
        return None

