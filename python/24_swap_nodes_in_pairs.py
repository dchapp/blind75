# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursive(head)
    
    
    def recursive(self, head):
        if head is None or head.next is None:
            return head
        current = head
        successor = head.next
        subproblem = head.next.next
        # Make successor the new head
        successor.next = current
        current.next = self.recursive(subproblem)
        return successor
        
