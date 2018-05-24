class UnionFind:
  ''' 
  Implementation of Weighted Quick Union with Path Compression, Single Pass
  ''' 
  
  def __init__(self, N):
    self.N, self.size = N, [1]*N
    self.id = [i for i in range(N)]
    
  def union(self, p, q):
    '''Connects nodes p and q'''
    p_root, q_root = self.root(p), self.root(q)
    if p_root == q_root: return
    
    p_root_size, q_root_size = self.size[p_root], self.size[q_root]
    # make the smaller tree a subtree of the larger tree
    # update the size of the larger tree
    if p_root_size < q_root_size:
      self.size[q_root] += p_root_size 
      self.id[p_root] = q_root
    else: 
      self.size[p_root] += q_root_size
      self.id[q_root] = p_root 

  def connected(self, p, q):
    '''Is there a path between p and q?'''
    return self.root(p) == self.root(q)
  
  def root(self, i):
    while self.id[i] != i:
      # make node's grandparent its parent
      self.id[i] = self.id[self.id[i]] 
      # skip traversing the old parent
      # this halves time to find the root
      i = self.id[i]
    return i