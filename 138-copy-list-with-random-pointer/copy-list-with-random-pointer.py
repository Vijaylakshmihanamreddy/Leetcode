class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # STEP 1: Insert copied nodes in between
        curr = head
        while curr:
            new = Node(curr.val)
            new.next = curr.next
            curr.next = new
            curr = new.next

        # STEP 2: Assign random pointers
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next

        # STEP 3: Separate original and copied list
        curr = head
        copy_head = head.next
        copy = copy_head

        while curr:
            curr.next = curr.next.next
            if copy.next:
                copy.next = copy.next.next
            curr = curr.next
            copy = copy.next

        return copy_head
        