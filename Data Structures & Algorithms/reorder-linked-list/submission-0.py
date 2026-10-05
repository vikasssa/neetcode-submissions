# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next

            fast = fast.next.next

        
        head2 = slow.next
        slow.next = None

        prev = None
        curr = head2

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        head1 = head
        head2 = prev

        dummy = ListNode()
        curr = dummy
        while head1 and head2:
            curr.next = head1
            head1 = head1.next
            curr = curr.next

            curr.next = head2
            head2 = head2.next
            curr = curr.next
        
        curr.next = head1 or head2



