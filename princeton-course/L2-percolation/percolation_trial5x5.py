from random import randint
from numpy import mean, std, sqrt
from percolation_grid import PercolationGrid
from percolation_tests import PercolationGrid5x5Test

class PercolationTrial5x5:
  def __init__(self):
    pass

  def single_run(self, draw_each=False, draw_last=False):
    P, test, i = PercolationGrid(5), PercolationGrid5x5Test(), 0
    
    while P.does_percolate() == False:
    
      r, c = randint(1, 5), randint(1, 5)
    
      if P.is_cell_unblocked(r, c) == False:
        i+=1 
        P.unblock_cell(r, c)  
        if draw_each == True:
          print("#", i, "UNBLOCK: (", r, ", ", c, ")")
          test.draw(P)
            
    if draw_last == True:
      test.draw(P)
      print("threshold:", P.unblocked_cells_fraction())
    
    return P.unblocked_cells_fraction()

  def run_trials(self, t = 30):
    trials = []
    
    for _ in range(t):
      threshold = self.single_run()
      trials.append(threshold)
    
    m, s = mean(trials), std(trials, ddof=1)
    i =  1.96 * s / sqrt(t)
    lo, hi = m - i, m + i
    
    print("mean:  ", m)
    print("stdev: ", s)
    print("0.95lo:", lo)
    print("0.95hi:", hi)