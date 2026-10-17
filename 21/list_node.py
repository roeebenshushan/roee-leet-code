class ListNode:
    value: int
    next: ListNode | None
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
