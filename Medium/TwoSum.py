class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)

def arrayToLinkedList(arr):
    dummy = ListNode(0)
    curr = dummy
    for num in arr:
        curr.next = ListNode(int(num))  # Convert to int to handle float inputs
        curr = curr.next
    return dummy.next

def printLinkedList(node):
    current = node
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    return '->'.join(result)
    
class Solution(object):
    def addTwoNumbers(self, l1:ListNode, l2:ListNode):
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next

test = Solution()
list1 = arrayToLinkedList([2, 4, 3])
list2 = arrayToLinkedList([5, 6, 4])
result = test.addTwoNumbers(list1, list2)
print(printLinkedList(result)) 