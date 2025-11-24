# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        self.left = ListNode(0, head)

        def helper(head):
            if not head:
                return True

            right = helper(head.next)
            self.left = self.left.next

            return right and self.left.val == head.val
        return helper(head)


def build_list(values):
    dummy = ListNode()
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

# Example test
head = build_list([2, 1, 1, 1, 2])
solution = Solution()
print(solution.isPalindrome(head))
