# Definition for singly-linked list.
from Tools.scripts.generate_opcode_h import header


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        list_vals = []

        while head:
            list_vals.append(head.val)
            head = head.next

        return all(list_vals[i] == list_vals[~i] for i in range(len(list_vals) // 2))


node = None
while head:
    temp = head.next
    head.next = node
    node = head
    head = temp

return node
