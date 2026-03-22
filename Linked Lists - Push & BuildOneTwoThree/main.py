class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    # Your code goes here.
    res = Node(data)
    res.next = head
    return res

def build_one_two_three():
    # Your code goes here.
    chained = None
    chained = push(chained, 3)
    chained = push(chained, 2)
    chained = push(chained, 1)
    return chained
