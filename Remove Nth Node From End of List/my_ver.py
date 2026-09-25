class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        curr = head
        length = 0

        while curr:
            length += 1
            curr = curr.next

        pos = length - n + 1
        
        if pos == 1:
            return head.next

        curr = head

        while pos - 1 > 1:
            curr = curr.next
            pos -= 1

        curr.next = curr.next.next

        return head
