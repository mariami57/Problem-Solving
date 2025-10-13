# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stack1, stack2 = [], []

        def fill_stack(stack, cur):
            while cur:
                stack.append(cur)
                cur = cur. next

        fill_stack(stack1, headA)
        fill_stack(stack2, headB)

        prev = None
        while stack1 and stack2:
            node1, node2 = stack1.pop(), stack2.pop()
            if node1 == node2:
                prev=node1

        return prev




