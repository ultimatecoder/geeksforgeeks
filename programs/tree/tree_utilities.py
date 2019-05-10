#! /usr/bin/env python

from tree import node


def insert_key(tree, parent, key, side):
    """Inserts key as a child at parent of the tree

    Arguments:
        * tree   : An instance of binary_tree.Tree
        * parent : Key value of the parent
        * key    : Value of key to be inserted as child of parent
        * side   : The value of side can be 'L' or 'R'. The value 'L' will add
                   child key as the left child of the parent. The 'R' will add
                   child key as the right child of the parent.

    Raises:
        * `KeyError` if parent key is not found
        * `ValueError` if vlaue of size is different then values 'L' and 'R'.
    """
    if side not in ('L', 'R'):
        raise ValueError(
            f"The value of side can be 'L' or 'R', but not {side}"
        )

    if tree.root is None:
        tree.root = node.Node(parent)
    if side == 'L':
        tree.insert_left_child(parent, key)
    else:
        tree.insert_right_child(parent, key)


def parse(pairs):
    """Parses given input into batch of 3 values.

    Example:
    >>>parse(["10", "20", "L", "10", "30", "R"]) == [
    (10, 20, "L"), (10, 30, "R")
    ]
    """
    result = []
    gap = 3
    window = gap
    start = 0
    for _ in range(len(pairs)//3):
        pair = pairs[start:window]
        result.append((int(pair[0]), int(pair[1]), pair[2]))
        start = window
        window += gap
    return result
