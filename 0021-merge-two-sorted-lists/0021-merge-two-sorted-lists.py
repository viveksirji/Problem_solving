# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
        stack=[]
        while list1:
            stack.append(list1.val)
            list1=list1.next
        while list2:
            stack.append(list2.val)
            list2=list2.next
        stack.sort()
        curr=dummy=ListNode()
        for i in stack:
            curr.next=ListNode(i)
            curr=curr.next
        return dummy.next
        


        