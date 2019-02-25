from queue import Queue

class Node:
    def __init__(self, k, v):
        self.key, self.value = k, v
        self.left, self.right = None, None
        self.count = 1

    @staticmethod
    def put(k, v, current):
        if current is None: return Node(k, v)
        if k < current.key:
            current.left = Node.put(k, v, current.left)
        elif k > current.key:
            current.right = Node.put(k, v, current.right)
        else: # equal
            current.value = v
        # update node's count
        current.count = 1 + Node.size(current.left) + Node.size(current.right)
        return current

    @staticmethod
    def size(current):
        if current is None: return 0
        return current.count

    @staticmethod
    def updated_size(current):
        return 1 + Node.size(current.left) + Node.size(current.right)

    @staticmethod
    def floor(k, current):
        if current is None: return None
        if k == current.key: return current
        if k < current.key: # the floor(node) MUST be on the left
            return Node.floor(k, current.left)
        # if k > current.key then floor(key) COULD be on the right
        # or it could be the node itself.
        candidate_node = Node.floor(k, current.right)
        if candidate_node is not None:
            return candidate_node
        else:
            return current

    @staticmethod
    def ceiling(k, current):
        if current is None: return None
        if k == current.key: return current
        if k > current.key: #ceiling MUST be on the right
            return Node.ceiling(k, current.right)
        # if k < current.key then floor(key) COULD be on left
        # or it could be the node itself
        candidate_node = Node.ceiling(k, current.left)
        if candidate_node is not None:
            return candidate_node
        else:
            return current

    @staticmethod
    def select(n, current):
        t = Node.size(current.left)
        if n < t: return Node.select(n, current.left)
        elif n > t: return Node.select(n - t - 1, current.right)
        return current

    @staticmethod
    def rank(k, current):
        if current is None: return 0
        if k < current.key: return Node.rank(k, current.left)
        if k > current.key:
            return 1 + Node.size(current.left) + Node.rank(k, current.right)
        # k == current.key
        return Node.size(current.left)

    @staticmethod
    def minimum(current):
        while current.left is not None:
            current = current.left
        return current

    @staticmethod
    def maximum(current):
        while current.right is not None:
            current = current.right
        return current

    @staticmethod
    def delete_minimum(current):
        if current.left is None: # current is the minimum, replace it by its right link
            return current.right
        # Recursively delete the minimum of current's left subtree if it exists
        current.left = Node.delete_minimum(current.left)
        # Update count of given subtree
        current.count = Node.updated_size(current)
        # the current node should be itself, unless it's the minimum, then it should
        # be replaced by its right link.
        return current

    @staticmethod
    def delete_maximum(current):
        if current.right is None: return current.left
        current.right = Node.delete_maximum(current.right)
        current.count = Node.updated_size(current)
        return current

    @staticmethod
    def delete(k, current):
        # If you've found nothing, then there's nothing to delete
        if current is None: return None
        if k < current.key: # search for key in left
            current.left = Node.delete(k, current.left)
        elif k > current.key: # search for key in right
            current.right = Node.delete(k, current.right)
        else: # you found the node!
            # Case1: You have at most one children
            if current.right is None: return current.left
            if current.left is None: return current.right
            # Case2: You have two children
            # Find and get replaced by your "successor"
            node_k = current
            current = Node.minimum(node_k.right)
            current.right = Node.delete_minimum(node_k.right)
            current.left = node_k.left
        current.count = Node.updated_size(current)
        return current

    @staticmethod
    def height(current):
        if current is None: return -1
        return 1 + max(Node.height(current.left), Node.height(current.right))


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.q = None # storage for inorder traversal

    def __iter__(self):
        self.q = Queue()
        self._inorder(self.root) # populates self.q
        return self

    def __next__(self):
        if self.q.empty(): raise StopIteration
        return self.q.get()

    def _inorder(self, current):
        if current is None: return
        self._inorder(current.left)
        self.q.put(current.key)
        self._inorder(current.right)

    def inorder_queue():
        self.__iter__()
        return self.q

    def levelorder_queue(self):
        keys = Queue()
        nodes = Queue()
        nodes.put(self.root)
        while not nodes.empty():
            current = nodes.get()
            if current is None: continue
            keys.put(current.key)
            nodes.put(current.left)
            nodes.put(current.right)
        return keys

    @staticmethod
    def _check(k):
        if k is None: raise Exception('argument must not be None')

    def insert(self, k, v):
        BinarySearchTree._check(k)
        BinarySearchTree._check(k)
        self.root = Node.put(k, v, self.root)

    def get(self, k):
        # get value associated with key k if it exists
        BinarySearchTree._check(k)
        current = self.root
        while current is not None:
            if k < current.key:
                current = current.left
            elif k > current.key:
                current = current.right
            else: # equal
                return current.value
        return None

    def delete(self, k):
        BinarySearchTree._check(k)
        self.root = Node.delete(k, self.root)

    def is_empty(self):
        return self.root is None

    def height(self):
        #Note: height of one-node tree: 0, height of None: -1
        return Node.height(self.root)

    def rank(self, k):
        BinarySearchTree._check(k)
        return Node.rank(k, self.root)

    def select(self, n):
        if n >= self.size() or n < 0: return None
        return Node.select(n, self.root).key

    def does_contain(self, k):
        BinarySearchTree._check(k)
        if self.get(k) is None: return False
        return True

    def floor(self, k):
        # Get the largest key less than or equal to key k
        BinarySearchTree._check(k)
        node = Node.floor(k, self.root)
        if node is None: return None
        return node.key

    def ceiling(self, k):
        # Get the smallest key greater than or equal to key k
        BinarySearchTree._check(k)
        node = Node.ceiling(k, self.root)
        if node is None: return None
        return node.key

    def size(self):
        return Node.size(self.root)

    def size_between(self, lo_k, hi_k):
        BinarySearchTree._check(lo_k)
        BinarySearchTree._check(hi_k)
        if lo_k > hi_k: return 0
        if self.does_contain(hi_k):
            return self.rank(hi_k) - self.rank(lo_k) + 1
        return self.rank(hi_k) - self.rank(lo_k)

    def delete_minimum(self):
        if self.is_empty(): return
        self.root = Node.delete_minimum(self.root)

    def delete_maximum(self):
        if self.is_empty(): return
        self.root = Node.delete_maximum(self.root)

    def minimum(self):
        if self.is_empty(): return None
        return Node.minimum(self.root).key

    def maximum(self):
        if self.is_empty(): return None
        return Node.maximum(self.root).key
