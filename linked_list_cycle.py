# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast_p = head
        slow_p = head

        while fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

            if fast_p == slow_p:
                return True

        return False

