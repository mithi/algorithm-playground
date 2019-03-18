use UnionFind;

#[derive(Debug)]
pub struct QuickFind {
    pub n: usize, 
    pub id: Vec<usize>,
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


#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn test_simple_connected() {

        let mut q = QuickFind::new(10);
        
        let i = q.connected(4, 7);
        let j = q.connected(3, 6);
        let k = q.connected(1, 2);
        
        assert!(!i);
        assert!(!j);
        assert!(!k);
    }

    #[test]
    fn test_simple_union() {

        let mut q = QuickFind::new(10);

        q.union(4, 3);
        assert_eq!(q.id, vec![0, 1, 2, 3, 3, 5, 6, 7, 8, 9]);

        q.union(3, 8);
        assert_eq!(q.id, vec![0, 1, 2, 8, 8, 5, 6, 7, 8, 9]);

        let i = q.connected(4, 3);
        let j = q.connected(8, 3);
        let k = q.connected(4, 8);

        assert!(i);
        assert!(j);
        assert!(k);
    }
}