class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root):
    serial = [root.val]

    if root.left is None:
        pass
    else:
        serial.append(serialize(root.left))

    if root.right is None:
        pass
    else:
        serial.append(serialize(root.right))
    return serial


def deserialize(s):
    for index in range(len(s)):
        if type(s[index]) is list:
            s[index] = deserialize(s[index])

    return Node(*s)


if __name__ == "__main__":
    node = Node('root', Node('left', Node('left.left')), Node('right'))

    assert deserialize(serialize(node)).left.left.val == 'left.left'
