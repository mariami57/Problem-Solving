# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#         stack1, stack2 = [], []
#
#         def fill_stack(stack, cur):
#             while cur:
#                 stack.append(cur)
#                 cur = cur. next
#
#         fill_stack(stack1, headA)
#         fill_stack(stack2, headB)
#
#         prev = None
#         while stack1 and stack2:
#             node1, node2 = stack1.pop(), stack2.pop()
#             if node1 == node2:
#                 prev=node1
#
#         return prev


# class Solution:
#     def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
#
#         def find_length(cur):
#             length = 0
#             while cur:
#                 length += 1
#                 cur = cur.next
#             return length
#
#         length1 = find_length(headA)
#         length2 = find_length(headB)
#
#         while length1 > length2:
#             headA = headA.next
#             length1 -=1
#         while length1 < length2:
#             headB = headB.next
#             length2 -=1
#
#         while headA != headB:
#             headA = headA.next
#             headB = headB.next
#         return headA


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None

        a,b = headA, headB

        while a != b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a



