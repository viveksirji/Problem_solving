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
        head=dummy=ListNode()
        for i in stack:
            head.next=ListNode(i)
            head=head.next
        return dummy.next
       

       
        
        
      
        


        