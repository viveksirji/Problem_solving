# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
   
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        num1=[]
        num2=[]
        while l1:
            num1.append(str(l1.val))
            l1=l1.next

        while l2:
            num2.append(str(l2.val))
            l2=l2.next
        num1.reverse()
        num2.reverse()
        total=str(int("".join(num1))+int("".join(num2)))
        dummy=ListNode(0)
        current=dummy
        for digit in total[::-1]:
            current.next=ListNode(int(digit))
            current=current.next
        return dummy.next
        