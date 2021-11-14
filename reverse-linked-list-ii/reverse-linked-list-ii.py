# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        """
        
        Step 1: turn list to a list
        Step 2: take a sub array and reverse it 
        Step 3: turn back into linked list and return
        
        
        Time N + K + K + N = 2N +2K = N + K
        """
        #Space O(n) n size of list
        reverse = []
        #Time O(n) size of list
        while head:
            reverse.append(head.val)
            head = head.next
        #Time O(k) Where k is size of left right window Space O(k)
        sub = reverse[left-1:right]
        #Time O(k) Space O(k)
        sub = sub[::-1]
        rev_idx = left - 1
        # Time O(k)
        for i in range(len(sub)):
            reverse[rev_idx] = sub[i]
            rev_idx +=1
        dummy = head = ListNode()
        # O(n) 
        for num in reverse:
            dummy.next = ListNode(num)
            dummy = dummy.next
        return head.next
        
        
        
        
        