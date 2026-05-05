class Solution(object):
    def removeNthFromEnd(self, head, n):
        # Step 1: Find length
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        # Step 2: If head needs to be removed
        if n == length:
            return head.next

        # Step 3: Go to (L - n - 1) node
        curr = head
        for _ in range(length - n - 1):
            curr = curr.next

        # Step 4: Delete node
        curr.next = curr.next.next

        return head