"""
Paths with Sum: You are given a binary tree in which each node contains an integer value (which
might be positive or negative). Design an algorithm to count the number of paths that sum to a
given value. The path does not need to start or end at the root or a leaf, but it must go downwards
(traveling only from parent nodes to child nodes).
"""


def count_path_with_sum(root, target): # count all the possible path from every node
    if root is None:
        return 0

    paths_from_root = count_path_with_sum_from_node(root, target, 0)
    paths_from_left = count_path_with_sum(root.left, target)
    paths_from_right = count_path_with_sum(root.right, target)

    return paths_from_root + paths_from_left + paths_from_right


def count_path_with_sum_from_node(node, target, current_sum):
    if node is None:
        return 0
    current_sum += node.data
    total_path = 0

    if current_sum == target:
        total_path += 1

    total_path += count_path_with_sum_from_node(node.left, target, current_sum)
    total_path += count_path_with_sum_from_node(node.right, target, current_sum)
    return total_path

