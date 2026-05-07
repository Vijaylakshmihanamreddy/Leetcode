class Solution(object):
    def copyRandomList(self, head):
        if not head:
            return None

        # STEP 1: Insert copied nodes in between
        c = head
        while c:
            new = Node(c.val)
            new.next = c.next
            c.next = new
            c = new.next
        
        c =  head
        while c:
            if c.random:
                c.next.random = c.random.next
            c = c.next.next
        
        # create a head for clone
        clo_head = head.next

        c = head
        c1 = clo_head

        while c:
            c.next = c.next.next
            if c1.next:
                c1.next =c1.next.next
            c = c.next
            c1 = c1.next
        return clo_head




      