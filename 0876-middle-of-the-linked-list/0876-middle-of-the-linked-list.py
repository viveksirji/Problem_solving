class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        current = head

        # Collect all nodes into an array
        while current:
            nodes.append(current)
            current = current.next

        # Return the middle node
        return nodes[len(nodes) // 2]