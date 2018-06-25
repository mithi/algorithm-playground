pub trait UnionFind {
    fn new(n: usize) -> Self; 
    fn union(&mut self, p: usize, q: usize); 
    fn connected(&mut self, p: usize, q: usize) -> bool;
}

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

#[derive(Debug)]
pub struct QuickUnion {
    n: usize, 
    id: Vec<usize>,
}

impl QuickUnion {
    fn root(&mut self, i: usize) -> usize {
        let mut x = i;
        while self.id[x] != x { x = self.id[x] };
        x
    }
}

impl UnionFind for QuickUnion {

    fn new(n: usize) -> Self {
        let id: Vec<usize> = (0..n).collect();
        QuickUnion { n, id } 
    }
    
    fn connected(&mut self, p: usize, q: usize) -> bool {
        self.root(p) == self.root(q)
    }

    fn union(&mut self, p: usize, q: usize) {
        let (p_root, q_root) = (self.root(p), self.root(q));
        self.id[p_root] = q_root;
    }
}

