class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str) -> Node | None:
    if list_repr == 'None':
        return None
    prep_list = list_repr.split(' -> ')[:-1][::-1]
    cycle_list = list(map(int, prep_list))
    prev = None
    node = None

    for el in cycle_list:
        node = Node(el, prev)
        prev = node

    return node
