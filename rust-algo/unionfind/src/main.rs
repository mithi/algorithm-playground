extern crate unionfind;

use unionfind::{UnionFind, QuickFind, QuickUnion};

fn main() {

    println!("QuickFind!");
    let mut q = QuickFind::new(10);
    println!("{:?}", q);

    let i = q.connected(4, 7);
    let j = q.connected(3, 6);
    let k = q.connected(1, 2);

    println!("{} {} {}", i, j, k);

    q.union(4, 3);
    println!("{:?} ", q); // [0, 1, 2, 3, 3, 5, 6, 7, 8, 9]
    q.union(3, 8);
    println!("{:?} ", q); // [0, 1, 2, 8, 8, 5, 6, 7, 8, 9]

    let i = q.connected(4, 3);
    let j = q.connected(8, 3);
    let k = q.connected(4, 8);

    println!("{} {} {}", i, j, k);

// -------------------------------------------------------------

    println!("QuickUnion!");
    let mut q = QuickUnion::new(10);
    println!("{:?}", q);

    let i = q.connected(4, 7);
    let j = q.connected(3, 6);
    let k = q.connected(1, 2);

    println!("{} {} {}", i, j, k);

    q.union(4, 3);
    println!("{:?} ", q); // [0, 1, 2, 3, 3, 5, 6, 7, 8, 9]
    q.union(3, 8);
    println!("{:?} ", q); // [0, 1, 2, 8, 3, 5, 6, 7, 8, 9]

    let i = q.connected(4, 3);
    let j = q.connected(8, 3);
    let k = q.connected(4, 8);

    println!("{} {} {}", i, j, k);
}
