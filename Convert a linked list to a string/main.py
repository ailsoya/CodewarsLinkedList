def stringify(node):
    probe = node
    res = []
    while probe is not None:
        res.append(str(probe.data))
        probe = probe.next
    res.append('None')
    return ' -> '.join(res)
