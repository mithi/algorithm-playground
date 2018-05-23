class WQUPathCompressionSinglePassUF:
  def __init__(self, N):
    self.N, self.id, self.size = N, [i for i in range(N)], [1]*N
        
  def union(self, p, q):
    p_root, q_root = self.root(p), self.root(q)
    if p_root == q_root: return
    
    p_root_size, q_root_size = self.size[p_root], self.size[q_root]
    if p_root_size < q_root_size:
      self.size[q_root] += p_root_size 
      self.id[p_root] = q_root
    else: 
      self.size[p_root] += q_root_size
      self.id[q_root] = p_root 

  def connected(self, p, q):
    return self.root(p) == self.root(q)
  
  def root(self, i):
    while self.id[i] != i:
      # make the grandparent of the node its parent
      self.id[i] = self.id[self.id[i]] 
      # skip traversing the old parent, halves time to find the root
      i = self.id[i]
    return i


# -------------------------------------------------------------------------------------


class WQUPathCompressionTwoPassUF:
  def __init__(self, N):
    self.N, self.id, self.size = N, [i for i in range(N)], [1]*N
        
  def union(self, p, q):
    p_root, q_root = self.root(p), self.root(q)
    if p_root == q_root: return
    
    p_root_size, q_root_size = self.size[p_root], self.size[q_root]
    if p_root_size < q_root_size:
      self.size[q_root] += p_root_size 
      self.id[p_root] = q_root
    else: 
      self.size[p_root] += q_root_size
      self.id[q_root] = p_root 

  def connected(self, p, q):
    return self.root(p) == self.root(q)
  
  def root(self, i):
    nodes = []

    while self.id[i] != i:
      nodes.append(i) # collect all nodes in path 
      i = self.id[i]
    
    # make all nodes in path point to root
    for j in nodes: 
      self.id[j] = i 
    
    return i