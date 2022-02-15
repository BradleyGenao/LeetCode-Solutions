# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head
        
        def get_mid(turtle):
            hare = turtle.next
            
            while hare and hare.next:
                turtle = turtle.next
                hare = hare.next.next
            return turtle
            
        def merge(l1, l2):
            dummy = ans = ListNode(-1)
            
            while l1 and l2:
                if l1.val < l2.val:
                    dummy.next = l1
                    l1 = l1.next
                else:
                    dummy.next = l2
                    l2 = l2.next
                dummy = dummy.next
            if l1:
                dummy.next = l1
            if l2:
                dummy.next = l2
            return ans.next
                    
        
        
        
        
        
        left = head
        right = get_mid(head)
    
        temp = right.next
        right.next = None 
        right = temp
        
        left = self.sortList(left)
        right = self.sortList(right)
        
        return merge(left, right)
        