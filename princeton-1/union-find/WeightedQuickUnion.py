class WeightedQuickUnionUF:
  def __init__(self, N):
    self.N, self.id, self.size = N, [], []
    for k in range(self.N):
      self.id.append(k)
      self.size.append(1)
        
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
    while self.id[i] != i: i = self.id[i]
    return i


# -------------------------------------------------------------------------------------


class WeightedQuickUnionTests:
  def __init__(self):
    self.N = 1 #number of cases
    self.case = [None for i in range(self.N)]
    # "8-7 7-0 9-6 5-4 4-6 8-3 1-0 7-6 7-2"
    self.case[0] = {
      'connections': [(4, 3), (3, 8), (6, 5), (9, 4), (2, 1), (8, 9),
        (5, 0), (7, 2), (6, 1), (7, 3)],
      'id': [6, 2, 6, 4, 6, 6, 6, 2, 4, 4]
    }
          
  def split_case(self, k):
    connections = self.case[k]['connections']
    correct_id = self.case[k]['id']
    N = len(correct_id)

    return N, connections, correct_id
    
  def run_test(self, k):
    N, connections, correct_id = self.split_case(k)
    UF = WeightedQuickUnionUF(N)
        
    for x, y in connections:
      UF.union(x, y)
    return UF.id == correct_id
          
  def run_all_tests(self):
    for k in range(self.N):
      if self.run_test(k) is False:
        print("TEST FAILED: CASE", k)
      else:
        print("TEST PASSED: CASE", k)
  