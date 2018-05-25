from union_find import UnionFind

class PercolationGrid:
  '''
  - percolation system model: n-by-n grid of cells. 
    - each cell (r, c) :  unblocked or blocked. 
    - top left cell: cell(1, 1) 
    - bottom right cell: cell(n, n) 
  - A system percolates if:
    - we fill all unblocked cells connected to the top row
    and that process fills some open cell on the bottom row.
  '''
  
  def __init__(self, n):
    '''Creates an n x n grid, with all cells blocked initially'''
    self.n = n
    self.cell_count = n * n
    self.unblocked_cell_count = 0
    self.fraction_of_cells_unblocked = 0.0
    
    # Each cell has a corresponding node number IE 
    # cell at row = 1, column = 1 -> node = 1 
    # cell at row = 1, column = 2 -> node = 2 
    # cell at row = 2, column = n -> node = 2 * n
    # cell at row = n, column = n -> node = n * n  
    # - node 0 - connects to open all top row cells 
    # - node n*n + 1 - connects to  all open bottom row cells    
    self.node_count = self.cell_count + 2

    # Initializes a Tree object that:
    # - Efficiently connects two cells
    # - Efficiently finds if two cells are connected 
    # Each cell represented as a node (number)
    self.UFTree = UnionFind(self.node_count)
    
    # List index: node(number) 
    # Corresponding value: unblocked(True), blocked(False)
    # Initially, all nodes (cells) are blocked 
    self.is_node_unblocked = [False for i in range(self.node_count)]
      
  def unblocked_cells_fraction(self):
    '''Number of unblocked cells over total number of cells'''
    return self.unblocked_cell_count / self.cell_count 
    
  def does_percolate(self):
    ''' 
    Is there a path from the cells in the top row to 
    the cells in the bottom row? 
    '''
    return self.UFTree.connected(0, self.cell_count + 1)

  def is_cell_unblocked(self, r, c):
    '''Is cell unblocked?'''
    i = self.cell_to_node(r, c)
    return self.is_node_unblocked[i]

  def unblock_cell(self, r, c):
    '''
    Unblock cell at row r and column c, if blocked.
    Connect this cell to all open neighboring nodes
    '''
    # make sure that values given makes sense
    self.check_scope(r, c) 
    # get node representation of cell
    current = self.cell_to_node(r, c)
    # don't do anything, if the given cell's unblocked
    if self.is_node_unblocked[current] is True: return
    # mark node as unblocked
    self.is_node_unblocked[current] = True
    # remember to update the running unblocked cell total 
    self.unblocked_cells_count += 1
    # connect the node to its neighbors
    self.connect_unblocked_neighbors(self, current, r, c)
    
  def connect_unblocked_neighbors(self, current, r, c):
    '''
    Connect the node to its left, right, top, and bottom 
    neighbors given they exist and are not blocked
    '''
    
    # connect node current to its left and right neighbors 
    if c != 1: 
      left = self.cell_to_node(r, c - 1)
      self.connect_nodes(current, left)
    if c != self.n: 
      right = self.cell_to_node(r, c + 1)
      self.connect_nodes(current, right)
    
    # connect node to its top and bottom neighbors
    # if the node is at the most top row connect it to 
    # the "virtual top node" 
    # if the node is at the most bottom row, connect it to 
    # the "virtual bottom node"
    top, bottom = 0, self.cell_count + 1 
    
    if r != 1: top = self.cell_to_node(r - 1, c)
    if r != self.n: bottom = self.cell_to_node(r + 1, c)
    
    self.connect_nodes(current, top)
    self.connect_nodes(current, bottom)
    
  def connect_nodes(self, i, j):
    '''Connect two node i, j if both nodes are unblocked'''
    if self.is_node_unblocked[i] and self.is_node_unblocked[j]:
      self.UFTree.connect(current, other)    
    
  def cell_to_node(self, r, c):
    '''Node representing cell located at row r, column c'''
    return (r - 1) * self.n + c  
    
  def node_to_cell(self, i):
    '''Tuple location tuple, (row, column) representing cell
       that corresponds to node i'''
    r, c = divmod(i - 1, self.n)
    return r + 1, c + 1
       
  def check_scope(self, r, c):
    '''
    Assert error if either row or column is
    incorrect type or not within range 
    '''
    out_of_scope_message =  "%r ...Not between 0 and " + str(self.n)
    c_message = "c: " + out_of_scope_message
    r_message = "r: " + out_of_scope_message

    assert type(r) is int, "r: %r ...Not an integer" % r
    assert type(c) is int, "c: %r ...Not an integer" % c
    assert 0 < c <= self.n, c_message % r
    assert 0 < r <= self.n, r_message % r