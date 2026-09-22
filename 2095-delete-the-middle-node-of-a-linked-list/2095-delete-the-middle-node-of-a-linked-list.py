class Solution:
    def deleteMiddle(self, head: ListNode | None) -> ListNode | None:
        if head.next is None:
            return None
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        mid = len(values) // 2
        values.pop(mid)
        current = head
        for value in values:
            current.val = value
            if current.next.next is None:
                current.next = None
                break
            current = current.next
        return head