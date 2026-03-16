class Solution(object):
    def swapNodes(self, head, k):
        # find length
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        
        first = head
        second = head
        
        # move first to kth node
        for _ in range(k-1):
            first = first.next
        
        # move second to (n-k+1)th node
        for _ in range(n-k):
            second = second.next
        
        # swap values
        first.val, second.val = second.val, first.val
        
        return head