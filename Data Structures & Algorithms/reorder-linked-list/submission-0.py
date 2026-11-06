# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        current = head
        array = []
        newArray = []
        j = 0
        while current is not None:
            array.append(current.val)
            current = current.next
        for i, x in enumerate(array):
            newArray.append(0)
            if (i+1)%2==0:
                newArray[i] = array[len(array)-j]
            else:
                newArray[i] = array[j]
                j = j + 1
        current = head
        for y in newArray:
            current.val = y
            current = current.next