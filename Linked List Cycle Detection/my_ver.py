# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head):
        seen = set()
        curr = head

        while curr:
            if curr in seen:
                return True
                break
            
            seen.add(curr)
            curr = curr.next
        
        return False
