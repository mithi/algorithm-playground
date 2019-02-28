# Left Leaning Red Black Binary Search Tree
- A binary search tree 
- No node has two red links connected to it 
- Every path from root to null link has the same number of black links
- Red links lean left
- Observation: search is the same as for elementary BST (ignores color) as well floor, iteration, selection, rank 
- To change: delete the minimum, delete the maximum, delete, insert 
- A binary search tree is a tree structure where all the keys on the left
- IMPORTANT: DELETION is not hibbard's deletion 
- A binary tree is either: empty or to dijoint binary trees (left and right) 
- A binary search is a binary tree in symmetric order
- Symmetric order: each node has a key and every node's key is larger than all keys in its left subtree and smaller than all keys in its right subtree.
- A BST is a reference to a root Node, a Node is comprised of for fields, a key and a value, and a reference to the right and left subtrees 

# Tests

### Test client
```

S E A R C H E X A M P  L  E
0 1 2 3 4 5 6 7 8 9 10 11 12

 *  A 8
 *  C 4
 *  E 12
 *  H 5
 *  L 11
 *  M 9
 *  P 10
 *  R 3
 *  S 0
 *  X 7
```

### Integrity of red-black tree data stuctures

```
1. is_BST(node, min_key, max_key) 
- is the tree root at x, a BST with all keys strictly between min and max. 
- if min and max is None, treat as empty constraint 

2. [RedBlackTree] is23(node):
  - tree have no consecutive red links 
  - no red links at the right

3. [RedBlackTree] is_balanced(node)
- all paths from the root has the same black edges

4. [RedBlackTree] is_RedBlackTree():
- is23()
- is_bst()
- is_balanced()
```