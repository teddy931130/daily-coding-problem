class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def count_unival_trees(root, count):
    unival_trees = count

    root_val = root.val
    left_branch = root.left
    right_branch = root.right

    if left_branch:
        same_value = (left_branch.val == root_val)
        if same_value:
            unival_trees[0] += 1

        count_unival_trees(left_branch, unival_trees)

    if right_branch:
        same_value = (right_branch.val == root_val)
        if same_value:
            unival_trees[0] += 1

        count_unival_trees(right_branch, unival_trees)

    return unival_trees


if __name__ == "__main__":
    node = Node(0, Node(1), Node(0, Node(1, Node(1), Node(1)), Node(0)))

    unival_trees_count = [0]
    print(sum(count_unival_trees(node, unival_trees_count)))
