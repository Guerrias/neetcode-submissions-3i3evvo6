# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        prev = None

        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next

        if not prev :
            return
        prev.next = None
        reversedHalf = self.reversedList(slow)  
        head = self.mergeList(head, reversedHalf)

    def reversedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reversed = None
        while head:
            temp = head.next
            head.next = reversed
            reversed = head
            head = temp
        return reversed

    def mergeList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(-1)
        tail = dummyHead
        i = 0

        while list1 and list2:
            if i % 2 == 0:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
            i += 1
        
        tail.next = list1 if list1 else list2
        return dummyHead.next