class Solution:
    def reverseList(self, head):
        curr = head
        prev = None
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
    
        # stack = []
        # curr = head
        
        # while curr:
        #     stack.append(curr)
        #     curr = curr.next
            
        # if not stack:
        #     return None
        
        # newhead = stack.pop()
        # curr = newhead
        # while stack:
        #     curr.next = stack.pop()
        #     curr = curr.next
        
        # curr.next = None
        
        # return newhead
            
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next    
        
rev = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
newhead = rev.reverseList(head)
curr = newhead

while curr:
    print(curr.val, end = '->' if curr.next else '\n')
    curr = curr.next