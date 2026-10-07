# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1 = head
        p2 = head
        while p2 is not None:
            if p2.next is not None: 
                p2 = p2.next.next
            else:
                break
            if p1 == p2:
                return True
            p1 = p1.next
        return False