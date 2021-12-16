# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        
        sent = ListNode(0)
        
        sent.next = head
        
        prev, curr = sent, head
        
        while curr and curr.next:
            if curr.val == curr.next.val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return sent.next
        