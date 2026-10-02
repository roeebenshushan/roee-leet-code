from list_node import ListNode


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    n0 = ListNode()
    n = n0
    carry = 0

    while l1 or l2 or carry:
        sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
        carry = sum // 10
        n.next = ListNode(sum % 10)
        
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
        n = n.next

    return n0.next
