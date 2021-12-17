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
            
            
            temp.next = prev
            prev = temp
        
        if fast:
            slow = slow.next
            
        while prev and prev.val == slow.val:
            prev = prev.next 
            slow = slow.next
        return prev == None
        
        