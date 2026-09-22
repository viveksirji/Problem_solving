# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head.next is None:
            return None
        n=0
        current=head
        
        while current:
            n+=1
            current=current.next
        mid=n//2
        current=head
        for i in range(mid-1):
            current=current.next
        current.next=current.next.next
        return head
    
        