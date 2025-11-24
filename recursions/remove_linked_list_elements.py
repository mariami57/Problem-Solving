# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         if head is None:
#             return None
#
#         temp = ListNode(0)
#         temp.next = head
#         prev, curr = temp, head
#
#         while curr:
#
#             if curr.val == val:
#                 prev.next = curr.next
#             else:
#                 prev = curr
#
#             curr = curr.next
#         return temp.next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        head.next = self.removeElements(head.next, val)

        if head.val == val:
            return head.next

        return head