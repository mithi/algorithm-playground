from bst import BinarySearchTree
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
    bst = BinarySearchTree()
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


@pytest.fixture
def empty_bst():
    return BinarySearchTree()


###########################################################################################
def test_empty(empty_bst):
    assert empty_bst.height() == -1
    assert empty_bst.is_empty() == True
    assert empty_bst.size()==0


###########################################################################################


def test_insert(sample_bst):

    assert sample_bst.root.key=='S'
    assert sample_bst.root.left.key=='E'
    assert sample_bst.root.right.key=='X'
    assert sample_bst.root.right.left is None
    assert sample_bst.root.right.right is None
    e_node = sample_bst.root.left
    assert e_node.left.key=='A'
    assert e_node.right.key=='R'
    a_node = e_node.left
    assert a_node.left is None
    assert a_node.right.key=='C'
    h_node = e_node.right.left
    assert h_node.left.key=='G'
    assert h_node.right.key =='M'
    # R
    assert e_node.right.right is None
    # C
    assert a_node.right.left is None
    assert a_node.right.right is None
    # G
    assert h_node.right.left is None
    assert h_node.right.right is None
    # M
    assert h_node.right.left is None
    assert h_node.right.right is None


def test_get(sample_bst):
    assert sample_bst.get('A')==1
    assert sample_bst.get('B')==None
    assert sample_bst.get('C')==2
    assert sample_bst.get('D')==None
    assert sample_bst.get('E')==3
    assert sample_bst.get('F')==None
    assert sample_bst.get('G')==4
    assert sample_bst.get('H')==5
    assert sample_bst.get('J')==None
    assert sample_bst.get('K')==None
    assert sample_bst.get('L')==None
    assert sample_bst.get('M')==6
    assert sample_bst.get('N')==None
    assert sample_bst.get('O')==None
    assert sample_bst.get('P')==None
    assert sample_bst.get('Q')==None
    assert sample_bst.get('R')==7
    assert sample_bst.get('S')==8
    assert sample_bst.get('T')==None
    assert sample_bst.get('U')==None
    assert sample_bst.get('V')==None
    assert sample_bst.get('W')==None
    assert sample_bst.get('X')==9
    assert sample_bst.get('Y')==None
    assert sample_bst.get('Z')==None


def test_simple(sample_bst):
    assert sample_bst.minimum()=='A'
    assert sample_bst.maximum()=='X'
    assert sample_bst.is_empty()==False
    assert sample_bst.height()==4


def test_rank(sample_bst):
    assert sample_bst.rank('A')==0
    assert sample_bst.rank('B')==1
    assert sample_bst.rank('C')==1
    assert sample_bst.rank('D')==2
    assert sample_bst.rank('E')==2
    assert sample_bst.rank('F')==3
    assert sample_bst.rank('G')==3
    assert sample_bst.rank('H')==4
    assert sample_bst.rank('I')==5
    assert sample_bst.rank('J')==5
    assert sample_bst.rank('K')==5
    assert sample_bst.rank('L')==5
    assert sample_bst.rank('M')==5
    assert sample_bst.rank('N')==6
    assert sample_bst.rank('O')==6
    assert sample_bst.rank('P')==6
    assert sample_bst.rank('Q')==6
    assert sample_bst.rank('R')==6
    assert sample_bst.rank('S')==7
    assert sample_bst.rank('T')==8
    assert sample_bst.rank('U')==8
    assert sample_bst.rank('V')==8
    assert sample_bst.rank('W')==8
    assert sample_bst.rank('X')==8
    assert sample_bst.rank('Y')==9
    assert sample_bst.rank('Z')==9


def test_select(sample_bst):
    assert sample_bst.select(0)=='A'
    assert sample_bst.select(7)=='S'
    assert sample_bst.select(2)=='E'
    assert sample_bst.select(6)=='R'
    assert sample_bst.select(1)=='C'
    assert sample_bst.select(4)=='H'
    assert sample_bst.select(8)=='X'
    assert sample_bst.select(5)=='M'
    assert sample_bst.select(3)=='G'


def test_floor(sample_bst):
    assert sample_bst.floor('A')=='A'
    assert sample_bst.floor('B')=='A'
    assert sample_bst.floor('C')=='C'
    assert sample_bst.floor('D')=='C'
    assert sample_bst.floor('E')=='E'
    assert sample_bst.floor('F')=='E'
    assert sample_bst.floor('G')=='G'
    assert sample_bst.floor('H')=='H'
    assert sample_bst.floor('I')=='H'
    assert sample_bst.floor('J')=='H'
    assert sample_bst.floor('K')=="H"
    assert sample_bst.floor('L')=='H'
    assert sample_bst.floor('M')=='M'
    assert sample_bst.floor('N')=='M'
    assert sample_bst.floor('O')=='M'
    assert sample_bst.floor('P')=='M'
    assert sample_bst.floor('Q')=='M'
    assert sample_bst.floor('R')=='R'
    assert sample_bst.floor('S')=='S'
    assert sample_bst.floor('T')=='S'
    assert sample_bst.floor('U')=='S'
    assert sample_bst.floor('V')=='S'
    assert sample_bst.floor('W')=='S'
    assert sample_bst.floor('X')=='X'
    assert sample_bst.floor('Y')=='X'
    assert sample_bst.floor('Z')=='X'


def test_ceiling(sample_bst):
    assert sample_bst.ceiling('A')=='A'
    assert sample_bst.ceiling('B')=='C'
    assert sample_bst.ceiling('C')=='C'
    assert sample_bst.ceiling('D')=='E'
    assert sample_bst.ceiling('E')=='E'
    assert sample_bst.ceiling('F')=='G'
    assert sample_bst.ceiling('G')=='G'
    assert sample_bst.ceiling('H')=='H'
    assert sample_bst.ceiling('I')=='M'
    assert sample_bst.ceiling('J')=='M'
    assert sample_bst.ceiling('K')=='M'
    assert sample_bst.ceiling('L')=='M'
    assert sample_bst.ceiling('M')=='M'
    assert sample_bst.ceiling('N')=='R'
    assert sample_bst.ceiling('O')=='R'
    assert sample_bst.ceiling('P')=='R'
    assert sample_bst.ceiling('Q')=='R'
    assert sample_bst.ceiling('R')=='R'
    assert sample_bst.ceiling('S')=='S'
    assert sample_bst.ceiling('T')=='X'
    assert sample_bst.ceiling('U')=='X'
    assert sample_bst.ceiling('V')=='X'
    assert sample_bst.ceiling('W')=='X'
    assert sample_bst.ceiling('X')=='X'
    assert sample_bst.ceiling('Y')==None
    assert sample_bst.ceiling('Z')==None


def test_does_contain(sample_bst):
    assert sample_bst.does_contain('A')==True
    assert sample_bst.does_contain('B')==False
    assert sample_bst.does_contain('C')==True
    assert sample_bst.does_contain('D')==False
    assert sample_bst.does_contain('E')==True
    assert sample_bst.does_contain('F')==False
    assert sample_bst.does_contain('G')==True
    assert sample_bst.does_contain('H')==True
    assert sample_bst.does_contain('I')==False
    assert sample_bst.does_contain('J')==False
    assert sample_bst.does_contain('K')==False
    assert sample_bst.does_contain('L')==False
    assert sample_bst.does_contain('M')==True
    assert sample_bst.does_contain('N')==False
    assert sample_bst.does_contain('O')==False
    assert sample_bst.does_contain('P')==False
    assert sample_bst.does_contain('Q')==False
    assert sample_bst.does_contain('R')==True
    assert sample_bst.does_contain('S')==True
    assert sample_bst.does_contain('T')==False
    assert sample_bst.does_contain('U')==False
    assert sample_bst.does_contain('V')==False
    assert sample_bst.does_contain('W')==False
    assert sample_bst.does_contain('X')==True
    assert sample_bst.does_contain('Y')==False
    assert sample_bst.does_contain('Z')==False


def test_size(sample_bst):
    assert sample_bst.size()==9 #S
    assert sample_bst.root.right.count==1 #X
    assert sample_bst.root.left.count==7 #E
    assert sample_bst.root.left.left.count==2 #A
    assert sample_bst.root.left.left.right.count==1 #C
    assert sample_bst.root.left.right.count==4 #R
    assert sample_bst.root.left.right.left.count==3 #H
    assert sample_bst.root.left.right.left.left.count==1 #G
    assert sample_bst.root.left.right.left.right.count==1 #M
    assert sample_bst.size_between('C', 'T')==7
    assert sample_bst.size_between('C', 'S')==7
    assert sample_bst.size_between('D', 'S')==6
    assert sample_bst.size_between('D', 'T')==6
    assert sample_bst.size_between('G', 'N')==3


def test_delete_min_max(sample_bst):
    assert sample_bst.size()==9
    assert sample_bst.minimum()=='A'
    sample_bst.delete_minimum()
    assert sample_bst.size()==8
    assert sample_bst.minimum()=='C'
    assert sample_bst.size()==8
    assert sample_bst.maximum()=='X'
    sample_bst.delete_maximum()
    assert sample_bst.size()==7
    assert sample_bst.maximum()=='S'
    sample_bst.delete_maximum()
    assert sample_bst.size()==6
    assert sample_bst.root.key=='E'
    assert sample_bst.maximum()=='R'


def test_delete(sample_bst):
    assert sample_bst.size()==9
    sample_bst.delete('G')
    assert sample_bst.size()==8
    assert sample_bst.root.left.key=='E'
    sample_bst.delete('Z')
    assert sample_bst.size()==8
    assert sample_bst.root.left.key=='E'
    sample_bst.delete('E')
    assert sample_bst.size()==7
    assert sample_bst.root.left.key=='H'
    sample_bst.delete('B')
    assert sample_bst.size()==7
    assert sample_bst.root.left.key=='H'


def test_inorder_iteration(sample_bst):
    inorder = ['A', 'C', 'E', 'G', 'H', 'M', 'R', 'S', 'X']
    x = []
    for s in sample_bst: # inorder iteratioN
        x.append(s)
    assert x==inorder


def test_levelorder(sample_bst):
    levelorder = ['S', 'E', 'X', 'A', 'R', 'C', 'H', 'G', 'M']
    q = sample_bst.levelorder_queue()
    x = []
    while not q.empty():
        x.append(q.get())
    assert x==levelorder
