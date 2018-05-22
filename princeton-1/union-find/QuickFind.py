class QuickFindUF:
  def __init__(self, N):
    self.N, self.id = N, []
    
    for k in range(N):
      self.id.append(k)
    
  def union(self, p, q):
    if self.connected(p, q) is True: return
    
    pid = self.id[p]
    for k in range(self.N):
      if self.id[k] == pid:
        self.id[k] = self.id[q]
    
  def connected(self, p, q):
    return self.id[p] == self.id[q]


# -------------------------------------------------------------------------------------


class QuickFindTests:
  def __init__(self):
    self.N = 3 #number of cases
    self.case = [None for i in range(self.N)]
    
    self.case[0] = {
      'connections': [(4, 3), (3, 8), (6, 5), (9, 4), 
        (2, 1), (8, 9), (5, 0), (7, 2), (6, 1)],
      'id': [1, 1, 1, 8, 8, 1, 1, 1, 8, 8]
    }

    self.case[1] = {
      'connections': [(6, 3), (6, 5), (9, 5), (7, 0), (3, 1), (9, 4)],
      'id': [0, 4, 2, 4, 4, 4, 4, 0, 8, 4]
    }

    self.case[2] = {
      'connections': [(4, 7), (7, 8), (9, 7), (6, 5), (8, 6), (2, 0)],
      'id': [0, 1, 0, 3, 5, 5, 5, 5, 5, 5]
    }
    
    # 0-2 3-0 5-9 5-2 7-9 7-8
    # 9-1 8-0 6-1 4-0 6-0 1-7
    # 5-2 0-2 5-9 2-1 3-9 4-6
    # 2-7 9-6 8-1 5-9 0-8 9-1
    # 8-9 4-0 8-5 2-6 1-7 0-3
    
  def split_case(self, k):
    connections = self.case[k]['connections']
    correct_id = self.case[k]['id']
    N = len(correct_id)

    return N, connections, correct_id

  def run_test(self, k):
    N, connections, correct_id = self.split_case(k)
    UF = QuickFindUF(N)
        
    for x, y in connections:
      UF.union(x, y)
    
    return UF.id == correct_id
          
  def run_all_tests(self):
    for k in range(self.N):
      if self.run_test(k) is False:
        print("TEST FAILED: CASE", k)
      else:
        print("TEST PASSED: CASE", k)