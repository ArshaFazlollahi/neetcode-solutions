# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        stack = []
        while current is not None:
            stack.append(current.val)
            current = current.next
        current = head
        while len(stack) != 0:
            current.val = stack[-1]
            stack.pop()
            current = current.next
        return head