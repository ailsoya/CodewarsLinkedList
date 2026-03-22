class Node(object):
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

def reverse(head):
    probe = head
    new_nodes = None

    while probe is not None:
        new_nodes = Node(probe.data, new_nodes)
        probe = probe.next

    return new_nodes
