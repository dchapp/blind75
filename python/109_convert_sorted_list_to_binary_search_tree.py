
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head;
    fast = head;
    slow_prev = None
    # When fast gets to end of list, slow will be at middle of list
    while (fast is not None and fast.next is not None):
        slow_prev = slow
        slow = slow.next;
        fast = fast.next.next;
    return slow_prev, slow
        


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if head is None:
            return head
        if head.next is None:
            return TreeNode(val=head.val)
        
        prev, mid = middle_node(head)
        root = TreeNode(mid.val)
        if prev is not None:
            prev.next = None
            root.left = self.sortedListToBST(head)
        if mid.next is not None:
            root.right = self.sortedListToBST(mid.next)
            
        return root   
