// Implement primitive `SinglyLinkedList` stack for i32 numbers
// Code that can be copy-pasted and ran on https://play.rust-lang.org/
use std::mem;
use std::fmt;

struct SinglyLinkedList {
  head: Node,
  count: i32, 
}

enum Node {
  Empty, 
  Has(i32, Box<Node>),
}

impl SinglyLinkedList {

  fn new() -> Self {
    SinglyLinkedList { head: Node::Empty, count: 0 }
  }

  fn push(&mut self, i: i32) {
    let old_head = mem::replace(&mut self.head, Node::Empty);
    self.head = Node::Has(i, Box::new(old_head));
    self.count += 1;
  }
  
  fn peek(&mut self) -> Option<i32> {
    match self.head {
      Node::Has(i, _) => Some(i),
      _ => None,
    }
  }
  
  fn pop(&mut self) -> Option<i32> {
  
    let t = mem::replace(&mut self.head, Node::Empty);
    
    let i = match t {
      Node::Empty => return None,
      Node::Has(value, next_box) => { 
        self.head = *next_box;
        value
      },
    };
    
    self.count -= 1;
    Some(i)
  }
  
  fn number_of_nodes(&self) -> i32 {
    self.count
  }
}

impl fmt::Display for SinglyLinkedList {
  fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {

    let mut t = &self.head; 
    let mut s = String::new();
    s.push_str(&format!("({}) list:", self.count));

    while let Node::Has(val, next_box) = t {
      t = &*next_box;
      s.push_str(&format!(" {} ->", val));
    }
    
    s.push_str(" Empty.");
    write!(f, "{}", s)
  }
}

fn main() {

  let mut a = SinglyLinkedList::new();
  println!("{}", a);
  a.push(3); 
  println!("{}", a);
  
  let mut b = SinglyLinkedList::new();
  b.push(4);
  println!("{}", b);
  b.push(5);
  println!("{}", b);
  
  let mut c = SinglyLinkedList::new();
  c.push(10);
  c.push(11);
  c.push(12);
  println!("number of nodes: {} ", c.number_of_nodes());
  println!("{}", c);
  println!("{:?}", c.pop());
  println!("{}", c);

  let mut d = SinglyLinkedList::new();
  println!("{}", d);
  println!("{:?}", d.peek()); 
  println!("{:?}", d.pop());
  
/*
(0) list: Empty.
(1) list: 3 -> Empty.
(1) list: 4 -> Empty.
(2) list: 5 -> 4 -> Empty.
number of nodes: 3 
(3) list: 12 -> 11 -> 10 -> Empty.
Some(12)
(2) list: 11 -> 10 -> Empty.
(0) list: Empty.
None
None
*/
}