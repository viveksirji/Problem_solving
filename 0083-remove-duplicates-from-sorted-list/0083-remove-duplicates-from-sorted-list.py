## LeetCode 83 - Remove Duplicates from Sorted List
# Definition for singly-linked list:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return None

        seen = {head.val}
        current = head

        while current.next:
            if current.next.val in seen:
                # Skip the duplicate node
                current.next = current.next.next
            else:
                seen.add(current.next.val)
                current = current.next

        return head

        