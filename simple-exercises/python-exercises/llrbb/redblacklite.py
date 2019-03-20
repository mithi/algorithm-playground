RED, BLACK = True, False

class Node: 
    def __init__(self, key, value, color, size):
        self.k = key
        self.v = value 
        self.left, self.right = None, None
        self.color = color
        self.size = size
        
    @staticmethod
    def is_red(current):
        if current is None: return False
        return current.color == RED
    
    @staticmethod
    def is_black(current):
        return not Node.is_red(current)
    
    @staticmethod
    def size(current):
        if current is None: return 0;
        return current.size
    
    @staticmethod
    def rotate_left(current):
        assert current is not None
        assert Node.is_red(current.right)
        
        new_root = current.right 
        current.right = new_root.left
        new_root.left = current 
        new_root.color = current.color
        current.color = RED
        new_root.size = current.size 
        current.size = 1 + Node.size(current.left) + Node.size(current.right)
        return new_root 

    @staticmethod 
    def rotate_right(current):
        assert current is not None
        assert Node.is_red(current.left)
        
        new_root = current.left
        current.left = new_root.right
        new_root.right = current 
        new_root.color = current.color 
        current.color = RED
        new_root.size = current.size 
        current.size = 1 + Node.size(current.left) + Node.size(current.right)
        return new_root 
    
    @staticmethod
    def flip_colors(current):
        assert current is not None
        assert current.left is not None
        assert current.right is not None 
        assert current.left.color != current.color
        assert current.right.color != current.color 
        assert current.right.color == current.left.color
        current.color = not current.color 
        current.left.color = not current.left.color
        current.right.color = not current.right.color
    
    # make current.left or one of its childred red
    @staticmethod 
    def move_red_left(current):
        assert current is not None
        assert Node.is_red(current)
        assert Node.is_black(current.left)
        assert Node.is_black(current.left.left)
        Node.flip_colors(current)
        if Node.is_red(current.right.left):
            current.right = Node.rotate_right(current.right)
            current = Node.rotate_left(current.right)
            Node.flip_colors(current)
        return current
    
    # make current.right or one of its children red
    @staticmethod
    def move_red_right(current):
        assert current is not None
        assert Node.is_red(current) 
        assert Node.is_black(current.right)
        assert Node.is_black(current.right.left)
        Node.flip_colors(current)
        if Node.is_red(current.left.left):
            current = Node.rotate_right(current)
            Node.flip_colors(current)
        return current
        

    @staticmethod
    def balance(current):
        # fix right leaning links
        if Node.is_black(current.left) and Node.is_red(current.right):
            current = Node.rotate_left(current)
        if Node.is_red(current.left) and Node.is_red(current.left.left):
            current = Node.rotate_right(current)
        if Node.is_red(current.left) and Node.is_red(current.right):
            Node.flip_colors(current)
        # update size
        current.size = 1 + Node.size(current.left) + Node.size(current.right)
        return current

    @staticmethod 
    def put(current, k, v):
        if current is None:
            return Node(k, v, RED, 1)
        
        if k < current.k:
            current.left = Node.put(current.left, k, v)
        elif k > current.k:
            current.right = Node.put(current.right, k, v)
        else:
            current.v = v
            
        return Node.balance(current)

    @staticmethod
    def delete_min(current):
        if current.left is None: return None
        if Node.is_black(current.left) and Node.is_black(current.left.left):
            current = Node.move_red_left(current)
        current.left = Node.delete_min(current.left)
        return Node.balance(current)
    
    @staticmethod
    def delete_max(current):
        if Node.is_red(current.left):
            current = Node.rotate_right(current)
        if current.right is None:
            return None
        if Node.is_black(current.right) and Node.is_black(current.right.left):
            current = Node.move_red_right(current)
        current.right = Node.delete_max(current.right)
        return Node.balance(current)
    
    @staticmethod
    def minimum(current):
        if current.left is None:
            return current
        return Node.minimum(current.left)
            
    @staticmethod
    def maximum(current):
        if current.right is None:
            return current
        return Node.minimum(current.right)
    
    @staticmethod 
    def delete(current, k):
        if k < current.k: 
            if Node.is_black(current.left) and Node.is_black(current.left.left):
                current = Node.move_red_left(current)
            current.left = Node.delete(current.left, k)
        else: 
            if Node.is_red(current.left):
                current = Node.rotate_right(current)
            if k == current.k and current.right is None:
                return None
            if Node.is_black(current.right) and Node.is_black(current.right.left):
                current = Node.move_red_right(current)
            if k == current.k:
                new_minimum = Node.minimum(current.right)
                current.k, current.v = new_minimum.k, new_minimum.v
                current.right = Node.delete_min(current.right)
            else:
                current.right = Node.delete(current.right, k)
        return Node.balance(current)
                
        
class RedBlackTree:
    def __init__(self):
        self.root = None
        
    def is_empty(self):
        return self.root is None 
    
    def size(self):
        return Node.size(self.root)
    
    def insert(self, key, value):
        if key is None: return
        
        self.root = Node.put(self.root, key, value)
        self.root.color = BLACK
    
    def delete(self, key):
        if self.is_empty(): return
        if self.contains(key) is False: return 

        if Node.is_black(self.root.left) and Node.is_black(self.root.right):
            node.root = RED
        
        self.root = Node.delete(self.root)
        if self.is_empty() is False: self.root.color = BLACK 
        
    
    def delete_min(self):
        is self.is_empty(): return
        
        if Node.is_black(self.root.left) and Node.is_black(self.root.right):
            node.root = RED
        
        self.root = Node.delete_min(self.root)
        if self.is_empty() is False: self.root.color = BLACK 
    
    def delete_max(self):
        is self.is_empty(): return
        
        if Node.is_black(self.root.left) and Node.is_black(self.root.right):
            node.root = RED
        
        self.root = Node.delete_max(self.root)
        if self.is_empty() is False: self.root.color = BLACK 

    
    def get(self, key)
        if key is None: return None 
        current = self.root
        while current is not None:
            if key > current.key:
                current = current.right
            elif key < current.key:
                current = current.left
            else: 
                return current.value
        return None 
    
    def contains(self, key):
        return self.get(key) is not None

    