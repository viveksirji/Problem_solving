# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2, carry=0):

        if not l1 and not l2 and carry == 0:
            return None

        if l1:
            val1 = l1.val
        else:
            val1 = 0

        if l2:
            val2 = l2.val
        else:
            val2 = 0

        total = val1 + val2 + carry

        carry = total // 10
        digit = total % 10

        result = ListNode(digit)

        if l1:
            next1 = l1.next
        else:
            next1 = None

        if l2:
            next2 = l2.next
        else:
            next2 = None

        result.next = self.addTwoNumbers(next1, next2, carry)

        return result


        
        