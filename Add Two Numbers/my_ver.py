class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        first = ''
        second = ''
        
        while l1:
            first = str(l1.val) + first
            l1 = l1.next

        while l2:
            second = str(l2.val) + second
            l2 = l2.next

        ans = str(int(first) + int(second))
        dummy = ListNode(0)
        curr = dummy

        for i in range(len(ans) - 1, -1, -1):
            new = ListNode(int(ans[i]))
            curr.next = new
            curr = curr.next

        return dummy.next
