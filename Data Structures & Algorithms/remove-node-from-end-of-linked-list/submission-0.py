# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        current = head

        while current:
            count += 1
            current = current.next
        
        nthFromBegin = count - n + 1
        if nthFromBegin == 1:
            return head.next
            
        prev = None
        current = head

        while current:
            nthFromBegin -= 1
            if nthFromBegin == 0:
                prev.next = current.next
                return head
            prev = current
            current = current.next
        return None
