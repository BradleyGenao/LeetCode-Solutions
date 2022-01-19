# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        fast = slow = head
        prev = None
        
        while fast and fast.next:
            temp = slow
            
            slow = slow.next
            fast = fast.next.next
            
            nxt = temp.next
            temp.next = prev
            prev = temp
            temp = nxt
        
        if fast:
            slow = slow.next
            
        
        while prev and slow.val == prev.val:
            slow = slow.next
            prev = prev.next
        
        return prev == None