# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        queue = deque(lists)
        
        final_list = []
        
        while queue:
            
            for _ in range(len(queue)):
                current = queue.popleft()
                
                while current:
                    final_list.append(current.val)
                    current = current.next
        
        final_list = sorted(final_list)
        
        dummy = answer = ListNode()
        
        for num in final_list:
            dummy.next = ListNode(num)
            dummy = dummy.next
        return answer.next
        
        