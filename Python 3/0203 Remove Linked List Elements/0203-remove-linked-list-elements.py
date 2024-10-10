# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        curr = dummy.next
        prev = dummy

        while curr:
            if curr.val == val:
                curr = curr.next
                prev.next = curr
            else:
                prev = curr
                curr.next

        return dummy.next