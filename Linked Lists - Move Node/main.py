class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    if source is None:
        raise ValueError
    edited_s = source.next
    edited_d = Node(source.data)
    edited_d.next = dest
    return Context(edited_s, edited_d)
