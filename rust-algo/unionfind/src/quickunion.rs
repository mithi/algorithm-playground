use UnionFind;

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