class Node:
    def __init__(self, next=None):
        self.next = next

def swap_pairs(head):
    t_node = Node(next=head)
    prev = t_node

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        prev.next = second
        first.next = second.next
        second.next = first

        prev = first

    return t_node.next
