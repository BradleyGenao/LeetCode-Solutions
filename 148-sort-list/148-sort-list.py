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
             
        def merge(left, right):
            dummy = ans = ListNode(-1)
            while left and right:
                if left.val < right.val:
                    dummy.next = left
                    left = left.next
                else:
                    dummy.next = right
                    right = right.next
                dummy = dummy.next
            if left:
                dummy.next = left
            if right:
                dummy.next = right
            return ans.next


       
        left = head
        right = get_mid(head)
        temp = right.next
        right.next = None
        right = temp        

        left = self.sortList(left)
        right = self.sortList(right) 
        
        return merge(left, right)

        