# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head or not head.next:
            return True
        slow = fast = head
        reverse = None
        
        while fast and fast.next:
            
            temp = slow
            
            slow = slow.next 
            fast = fast.next.next
            
            
            temp.next = reverse
            reverse = temp
        
        if fast:
            slow = slow.next
            
        while reverse and slow.val == reverse.val:
            slow = slow.next
            reverse = reverse.next
        
        return reverse == None
        