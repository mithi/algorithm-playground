# IMPORTANT: UNTESTED
# redblacklite does not exist yet

from redblacklite import RedBlackTree
from redblacklite import Node
import pytest

#              S(8)
#             /    \
#           E(3)   X(9)
#          /   \
#      A(1)     R(7)
#         \     /
#        C(2) H(5)
#            /   \
#           G(4)  M(6)
@pytest.fixture
def sample_bst():
    bst = RedBlackTree()
    bst.insert('S', 8)
    bst.insert('E', 3)
    bst.insert('A', 1)
    bst.insert('R', 7)
    bst.insert('C', 2)
    bst.insert('H', 5)
    bst.insert('X', 9)
    bst.insert('M', 6)
    bst.insert('G', 4)
    return bst


#  A 8
#  C 4
#  E 12
#  H 5
#  L 11
#  M 9
#  P 10
#  R 3
#  S 0
#  X 7
@pytest.fixture
def sample_bst2():
    bst = RedBlackTree()
    # S E A R C H E X A M P  L  E
    # 0 1 2 3 4 5 6 7 8 9 10 11 12
    key_string = "S E A R C H E X A M P L E"
    keys = key_string.split(" ")
    for i, key in enumerate(keys):
        bst.insert(key, i)
    return bst


@pytest.fixture
def empty_bst():
    return RedBlackTree()

# Does the tree have no red right links 
# and at most one left red link in a row on any path?
def test_if_23tree(sample_bst, sample_bst2, empty_bst)
    def is23(current, root):
        if current is None: return True
        if Node.is_red(current.right): return False
        if current.key != root.key \
            and Node.is_red(current) and Node.is_red(current.left):
            return False
        return is23(current.left, root) and is23(current.right, root)
    
    assert is23(sample_bst.root, sample_bst.root)
    assert is23(sample_bst.root, sample_bst.root)
    assert is23(empty_bst.root, empty_bst.root)

# do all paths from root to leaf have the same number
# of black links/edges
def test_if_balanced(sample_bst, sample_bst2, empty_bst):
    def black_links_count(bst):
        count = 0
        current = bst.root 
        while current is not None: 
            if Node.is_red(current) is False: 
                count +=1
            current = current.left
        return count 
    
    def is_balanced(current, black_count):
        if current is None: return black_count == 0
        if Node.is_red(current) is False: black_count -= 1
        return is_balanced(current.left, black_count) and \
            is_balanced(current.right, black_count)
    
    assert is_balanced(sample_bst.root, black_links_count(sample_bst))
    assert is_balanced(sample_bst2.root, black_links_count(sample_bst2))
    assert is_balanced(empty_bst.root, black_links_count(empty_bst))


def test_if_bst(sample_bst, sample_bst2, empty_bst):
    def is_bst(current, key_min, key_max):
        if current is None: return True
        if key_min is not None and current.key <= key_min:
            return False
        if key_max is not None and current.key >= key_max:
            return False
        return is_bst(current.left, key_min, current.key) and \
            is_bst(current.right, current.key, key_max
    
    assert is_bst(sample_bst.root, None, None)
    assert is_bst(sample_bst2.root, None, None)
    assert is_bst(empty_bst.root, None, None)
    
    