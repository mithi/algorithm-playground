use std::cmp::PartialEq;

pub struct Link(Option<i32>);

impl PartialEq for Link {
  fn eq(&self, other: &Link) -> bool {
    match (self, other) {
      (Link(None), Link(None)) => true,
      (Link(Some(i)), Link(Some(j))) if i == j => true,
      _ => false,
    } 
  }
}

fn main() {

  let y = Link(None);
  let w = Link(None);
  let x = Link(Some(3));
  let z = Link(Some(3));
  let u = Link(Some(4));
  
  assert!(Link(None) == Link(None));
  assert!(Link(Some(3)) == Link(Some(3)));
  assert!(Link(Some(3)) != Link(Some(4)));
  
  assert!(x == z);
  assert!(z == x);

  assert!(z != u);
  assert!(x != u);

  assert!(u != z);
  assert!(u != x);

  assert!(y == w);
  assert!(w == y);

  assert!(y != x);
  assert!(y != z);
  assert!(y != u);

  assert!(w != x);
  assert!(w != z);
  assert!(w != u);

  assert!(x != y);
  assert!(z != y);
  assert!(u != y);
  
  assert!(x == x);
  assert!(y == y);
  assert!(z == z);
  assert!(w == w);
  assert!(u == u);
}