# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        nums=[]
        for head in lists:
            temp=head
            while temp:
                nums.append(temp.val)
                temp=temp.next
        nums.sort()
        dummy=ListNode()
        curr=dummy
        for x in nums:
            curr.next=ListNode(x)
            curr=curr.next
        return dummy.next
        