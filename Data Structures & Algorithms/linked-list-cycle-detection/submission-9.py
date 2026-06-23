# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        # i = 0
        while head:
            if head in visited:
                # if head.next is None:
                #     return False
                # print(visited[head.val])
                return True
            # visited[head] = i
            visited.add(head)
            head = head.next
            # i = i+1
        
        return False