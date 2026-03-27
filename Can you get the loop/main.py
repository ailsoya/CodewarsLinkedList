def loop_size(node):
    first = node.next
    second = node.next.next

    while first != second:
        first = first.next
        second = second.next.next

    loop_length = 1
    current = first.next

    while current != first:
        current = current.next
        loop_length += 1

    return loop_length
