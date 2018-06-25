extern crate unionfind;

use std::fmt::Debug;
use unionfind::{UnionFind, QuickFind, QuickUnion};

fn check_uf<T: UnionFind + Debug>(q: &mut T) {

    println!("{:?}", q);

    let i = q.connected(4, 7);
    let j = q.connected(3, 6);
    let k = q.connected(1, 2);

    println!("{} {} {}", i, j, k);

    q.union(4, 3);
    println!("{:?} ", q); 
    
    q.union(3, 8);
    println!("{:?} ", q);

    let i = q.connected(4, 3);
    let j = q.connected(8, 3);
    let k = q.connected(4, 8);

    println!("{} {} {}", i, j, k);
}


fn main() {

    println!("QuickFind!");
    let mut q = QuickFind::new(10);
    check_uf(&mut q);

    println!("QuickUnion!");
    let mut q = QuickUnion::new(10);
    check_uf(&mut q);
}
