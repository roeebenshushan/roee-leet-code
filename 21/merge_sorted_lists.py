from list_node import ListNode

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        holder = ListNode()
        new_list = holder
        
        while list1 and list2:
            if list1.val < list2.val:
                holder.next = ListNode(list1.val)
                list1 = list1.next
            else:
                holder.next = ListNode(list2.val)
                list2 = list2.next

            holder = holder.next

        holder.next = list1 or list2
        return new_list.next
