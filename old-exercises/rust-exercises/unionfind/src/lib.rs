mod quickfind; 
mod quickunion; 

pub use quickfind::QuickFind;
pub use quickunion::QuickUnion;

pub trait UnionFind {
    fn new(n: usize) -> Self; 
    fn union(&mut self, p: usize, q: usize); 
    fn connected(&mut self, p: usize, q: usize) -> bool;
}
