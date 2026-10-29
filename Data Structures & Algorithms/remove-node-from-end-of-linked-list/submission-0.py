# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        right = head
        dummy = ListNode()
        dummy.next = head
        while n > 0:
            right = right.next
            n -= 1
        
        left = head
        prev = dummy
        while right:
            prev = left
            left = left.next
            right = right.next
        
        prev.next = left.next
        left = None
        return dummy.next
        