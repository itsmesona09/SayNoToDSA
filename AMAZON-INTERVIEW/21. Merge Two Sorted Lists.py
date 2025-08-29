class Merge_Two_Sorted_Lists:
    def mergelists(self, l1, l2):
        newnode = ListNode()
        curr = newnode
        
        while l1 and l2:
            if l1.val <= l2.val:
                curr.next = l1
                l1 = l1.next
            else:
                curr.next = l2
                l2 = l2.next
            
            curr = curr.next
                
        if l1:
            curr.next = l1
        if l2:
            curr.next = l2
        
        return newnode.next
        
        # curr1, curr2 = l1, l2
        # arr = []

        # while curr1:
        #     arr.append(curr1.val)
        #     curr1 = curr1.next

        # while curr2:
        #     arr.append(curr2.val)
        #     curr2 = curr2.next

        # arr.sort()

        # newhead = ListNode(arr[0])
        # curr = newhead
        # for item in arr[1:]:
        #     curr.next = ListNode(item)
        #     curr = curr.next
            
        # return newhead

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
sorted = Merge_Two_Sorted_Lists()
l1 = ListNode(1, ListNode(2, ListNode(4)))
l2 = ListNode(1, ListNode(5, ListNode(6)))

newhead = sorted.mergelists(l1, l2)

curr = newhead

while curr:
    print(curr.val, end= '->' if curr.next else '\n')
    curr = curr.next