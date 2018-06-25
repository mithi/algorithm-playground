use UnionFind;

#[derive(Debug)]
pub struct QuickFind {
    n: usize, 
    id: Vec<usize>,
}

impl UnionFind for QuickFind {
    fn new(n: usize) -> Self {
        let id: Vec<usize> = (0..n).collect(); 
        QuickFind { n, id }
    }

    fn connected(&mut self, p: usize, q: usize) -> bool {
        self.id[p] == self.id[q]
    }

    fn union(&mut self, p: usize, q:usize) {
        
        if self.connected(p, q) { return; }

        let id_p = self.id[p];
        
        for k in 0..self.n {
            if self.id[k] == id_p { 
                self.id[k] = self.id[q]; 
            }
        }
    }
}