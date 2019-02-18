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


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_simple_connected() {

        let mut q = QuickUnion::new(10);
        
        let i = q.connected(4, 7);
        let j = q.connected(3, 6);
        let k = q.connected(1, 2);
        
        assert!(!i);
        assert!(!j);
        assert!(!k);
    }

    #[test]
    fn test_simple_union() {

        let mut q = QuickUnion::new(10);

        q.union(4, 3);
        assert_eq!(q.id, vec![0, 1, 2, 3, 3, 5, 6, 7, 8, 9]);

        q.union(3, 8);
        assert_eq!(q.id, vec![0, 1, 2, 8, 3, 5, 6, 7, 8, 9]);

        let i = q.connected(4, 3);
        let j = q.connected(8, 3);
        let k = q.connected(4, 8);

        assert!(i);
        assert!(j);
        assert!(k);
    }
}