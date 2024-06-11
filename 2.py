class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        head = ListNode()
        tmp_p = head
        remain = 0
        while p1 or p2 or remain != 0:
            tmp_sum = remain
            if p1:
                tmp_sum += p1.val
                p1 = p1.next
            if p2:
                tmp_sum += p2.val
                p2 = p2.next
            tmp_p.next = ListNode(tmp_sum % 10)
            tmp_p = tmp_p.next
            remain = tmp_sum // 10
        return head.next


def vector_to_listnode(vector):
    dummy_head = ListNode(0)
    current = dummy_head
    for val in vector:
        current.next = ListNode(val)
        current = current.next
    return dummy_head.next


# Input vectors
l1_vector = [2, 4, 3]
l2_vector = [5, 6, 4]

# Convert vectors to linked lists
l1 = vector_to_listnode(l1_vector)
l2 = vector_to_listnode(l2_vector)

solution = Solution()
result = solution.addTwoNumbers(l1, l2)

# Print the result linked list
while result:
    print(result.val, end=" -> " if result.next else "")
    result = result.next
