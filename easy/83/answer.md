```
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        
        prev_val = 0
        root = old_node = head
        
        while head:
            curr_val = head.val
            if curr_val == prev_val:
                old_node.next = head.next 
                head = head.next
                continue
            prev_val = curr_val
            old_node = head
            head = head.next
            
        return root
```
