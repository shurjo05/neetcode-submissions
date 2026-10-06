# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None: 
            return head
        curr = head.next
        prev = head
        prev.next = None
        if curr is None:
            return head
        nextNode = curr.next
        while curr is not None:
            curr.next = prev
            prev = curr
            curr = nextNode
            if nextNode is not None:
                nextNode = nextNode.next
        return prev