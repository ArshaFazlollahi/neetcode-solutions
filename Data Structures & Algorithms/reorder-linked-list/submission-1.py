# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        array = []
        j = 0
        while current is not None:
            array.append(current.val)
            current = current.next
        current = head
        for i, x in enumerate(array):
            if (i+1)%2==0:
                current.val = array[len(array)-j]
            else:
                current.val = array[j]
                j = j + 1
            current = current.next