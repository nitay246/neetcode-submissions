# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        j1 = j2 = head
        while j2 and j2.next:
            j2 = j2.next.next
            j1 = j1.next
            if j1 == j2:
                return True
        return False