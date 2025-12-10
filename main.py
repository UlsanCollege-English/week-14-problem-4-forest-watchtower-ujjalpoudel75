## main.py
"""
HW04 — Forest Watchtower (Balanced Tree Check)

Implement TreeNode and is_balanced(root) to check if a binary tree is height-balanced.
"""


class TreeNode:
    """
    Simple binary tree node: value, left, right.
    """

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_balanced(root):
    """
    Return True if the binary tree rooted at `root` is height-balanced.

    Empty tree (root is None) is considered balanced.
    """
    def check(node):
        if node is None:
            return True, 0
        left_balanced, left_height = check(node.left)
        right_balanced, right_height = check(node.right)
        balanced = (
            left_balanced and right_balanced and abs(left_height - right_height) <= 1
        )
        height = 1 + max(left_height, right_height)
        return balanced, height

    balanced, _ = check(root)
    return balanced


if __name__ == "__main__":
    # Optional: quick manual tree
    #   1
    #  / \
    # 2   3
    left = TreeNode(2)
    right = TreeNode(3)
    root = TreeNode(1, left, right)
    print(is_balanced(root))
