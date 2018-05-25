from percolation_grid import PercolationGrid

class PercolationGrid5x5Test: 
  def __init__(self):
    
    self.ncmap = {
      1: (1, 1),  2: (1, 2),  3: (1, 3),  4: (1, 4),  5: (1, 5),
      6: (2, 1),  7: (2, 2),  8: (2, 3),  9: (2, 4), 10: (2, 5),
     11: (3, 1), 12: (3, 2), 13: (3, 3), 14: (3, 4), 15: (3, 5),
     16: (4, 1), 17: (4, 2), 18: (4, 3), 19: (4, 4), 20: (4, 5),
     21: (5, 1), 22: (5, 2), 23: (5, 3), 24: (5, 4), 25: (5, 5),
    }
        
    self.P = PercolationGrid(5)
    
  def node_to_cell_test(self):
    
    for k, v in self.ncmap.items():
      r, c = self.P.node_to_cell(k)
      assert v == (r, c), "Not Equal: %r" % k
    print("node_to_cell(): Ok")
    
  def cell_to_node_test(self):
    for k, v in self.ncmap.items():
      r, c = v 
      i = self.P.cell_to_node(r, c)
      assert k == i, "Not Equal: i" % i 
    print("cell_to_node(): Ok")