from percolation_grid import PercolationGrid

class PercolationGrid5x5Test:
  '''
    .1  .2  .3  .4  .5
    +---+---+---+---+---+
  1 |  1|  2|  3|  4|  5|
    +---+---+---+---+---+
  2 |  6|  7|  8|  9| 10|
    +---+---+---+---+---+
  3 | 11| 12| 13| 14| 15|
    +---+---+---+---+---+
  4 | 16| 17| 18| 19| 20|
    +---+---+---+---+---+
  5 | 21| 22| 23| 24| 25|
    +---+---+---+---+---+
  '''
  def __init__(self):
    
    # maps node index to cell location (row, column) 
    self.node_cell = {
      1: (1, 1),  2: (1, 2),  3: (1, 3),  4: (1, 4),  5: (1, 5),
      6: (2, 1),  7: (2, 2),  8: (2, 3),  9: (2, 4), 10: (2, 5),
     11: (3, 1), 12: (3, 2), 13: (3, 3), 14: (3, 4), 15: (3, 5),
     16: (4, 1), 17: (4, 2), 18: (4, 3), 19: (4, 4), 20: (4, 5),
     21: (5, 1), 22: (5, 2), 23: (5, 3), 24: (5, 4), 25: (5, 5),
    }
    
  def cell_given_node_test(self):
    
    P = PercolationGrid(5)
    
    for k, v in self.node_cell.items():
      r, c = P.cell_given_node(k)
      assert v == (r, c), "FAIL! Not Equal: %r" % k
    print("cell_given_node(): Ok")
    
  def node_given_cell_test(self):
    
    P = PercolationGrid(5)
    for k, v in self.node_cell.items():
      r, c = v 
      i = P.node_given_cell(r, c)
      assert k == i, "FAIL! Not Equal: i" % i 
    print("node_given_cell(): Ok")
     
  def draw(self, P):
    '''
      .1  .2  .3  .4  .5
      +---+---+---+---+---+
    1 |  1|  2|  3|  4|  5|
      +---+---+---+---+---+
    2 |  6|  7|  8|  9| 10|
      +---+---+---+---+---+
    3 | 11| 12| 13| 14| 15|
      +---+---+---+---+---+
    4 | 16| 17| 18| 19| 20|
      +---+---+---+---+---+
    5 | 21| 22| 23| 24| 25|
      +---+---+---+---+---+
    '''
    
    grid_state = []
    for r in range(1, 6):
      row_state = []
      for c in range(1, 6):
        if P.is_cell_unblocked(r, c) == False:
          row_state.append(" x |")
        else:
          row_state.append("   |")
      grid_state.append(row_state)

    print("--------------------------------")
    print("      .1  .2  .3  .4  .5")
    
    for i, row_state in enumerate(grid_state):
      print("      +---+---+---+---+---+")
      print("    " + str(i) + " |", end="")
      for cell in row_state:
        print(cell, end="")
      print()
    print("      +---+---+---+---+---+")
    print("--------------------------------")
    
  def test_case_A(self, COL=1):
    
    print("----------------------------------")
    print("--- TEST CASE GIVEN COLUMN:", COL, "---")
    print("----------------------------------")

    assert 0 < COL < 6, "FAIL: Choose column between 1 and 5"
    P = PercolationGrid(5)

    print("All cells blocked initially...")
    for r in range(1, 6):
      for c in range(1, 6):
        assert P.is_cell_unblocked(r, c) == False, "FAIL! Unblocked at initialization" 
    print("...ok")
    
    print("Should NOT percolate...")
    assert P.does_percolate() == False, "FAIL! Did percolate."
    print("...ok")
    
    print("Unblock first row...")
    for c in range(1, 6): 
      P.unblock_cell(1, c)
      i = P.node_given_cell(1, c)
      assert P.UFTree.connected(0, i) == True, "FAIL! First row cell unconnected to virtual top cell"
      assert P.is_cell_unblocked(1, c) == True, "FAIL! Unblocked cell not marked as unblocked"
      assert P.are_connected(m = (1, 1), n = (1, c)) == True, "FAIL! Neighbors unconnected"     
    print("...ok")

    print("Should NOT percolate...")
    assert P.does_percolate() == False, "FAIL! Did percolate."
    print("...ok")

    print("Unblock last row...")
    for c in range(1, 6): 
      P.unblock_cell(5, c)
      i = P.node_given_cell(5, c)
      assert P.UFTree.connected(-1, i) == True, "FAIL! First row cell unconnected to virtual bottom cell"
      assert P.is_cell_unblocked(5, c) == True, "FAIL! Unblocked cell not marked as unblocked"
      assert P.are_connected(m = (5, 1), n = (5, c)) == True, "FAIL! Neighbors unconnected"     
    print("...ok")
    
    print("Should NOT percolate...")
    assert P.does_percolate() == False, "FAIL! Did percolate."
    print("...ok")

    print("Unblock given column...", COL)
    for r in range(1, 6):
      P.unblock_cell(r, COL)
      assert P.is_cell_unblocked(r, COL) == True, "FAIL! Unblocked cell not marked as unblocked"
      assert P.are_connected(m = (1, COL), n = (r, COL)) == True, "FAIL! Neighbors unconnected"
    print("...ok")
    
    print("All cells must be connected to corner cells...")
    print("All cells, must also be connected to virtual bottom and top nodes...")
    for r in range(1, 6):
      for c in range(1, 6):
        if P.is_cell_unblocked(r, c) == True:
          assert P.are_connected(m = (1, 1), n = (r, c)) == True, "FAIL! Cell unconnected to upperleft cell"
          assert P.are_connected(m = (5, 5), n = (r, c)) == True, "FAIL! Cell unconnected to lowerright cell"
          assert P.are_connected(m = (1, 5), n = (r, c)) == True, "FAIL! Cell unconnected to upperright cell"
          assert P.are_connected(m = (5, 1), n = (r, c)) == True, "FAIL! Cell unconnected to lowerleft cell"
          i = P.node_given_cell(r, c)
          assert P.UFTree.connected(-1, i) == True, "FAIL! Cell unconnected to virtual bottom cell"
          assert P.UFTree.connected(0, i) == True, "FAIL! Cell unconnected to virtual top cell"
        else:
          P.is_cell_unblocked(r, c) == False, "FAIL! Blocked cell marked as unblocked"
          i = P.node_given_cell(r, c)
          assert P.UFTree.connected(-1, i) == False, "FAIL! Cell connected to virtual bottom cell"
          assert P.UFTree.connected(0, i) == False, "FAIL! Cell connected to virtual top cell"

    print("...ok")
    
    print("Should percolate...")
    assert P.does_percolate() == True, "FAIL! Did not percolate."
    print("...ok")
