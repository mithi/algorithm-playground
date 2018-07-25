use std::mem;
type Link = Option<Box<Node>>;

struct List {
  head: Link,
  name: String
}

#[derive(Debug)]
struct Node {
  element: i32,
  next: Link,
}

impl Drop for Node {
  fn drop(&mut self) {
    println!(" --> Node: {} dropped.", self.element);
  }
}

impl List {

  fn new(given_name: &str) -> Self {
    println!("List: {} created.", given_name);
    List { head: None, name: String::from(given_name)}
  }

  fn push(&mut self, i: i32) {

    let old_head = self.head.take();    
    let new_node = Node { element: i, next: old_head };
    self.head = Some(Box::new(new_node));
  }
}

impl Drop for List {
  fn drop(&mut self) {
    println!("List: {} dropped.", self.name);
  }
}

fn main() {

  let mut a = List::new("First list");
  a.push(600);
  a.push(500);
  a.push(400);
  a.push(300);
  a.push(200);
  a.push(100);
  mem::drop(a);
  
  println!("-------------------------");
  let mut b = List::new("Second list");
  b.push(1);
  b.push(2);
  b.push(3);
  b.push(4);
  b.push(5);
  b.push(6);

  let mut c = List::new("Third list");
  c.push(10);
  c.push(20);
  c.push(30);
  c.push(40);
  c.push(50);
  c.push(60);
  
  println!("-------------------------");
}

/*
List: First list created.
List: First list dropped.
 --> Node: 100 dropped.
 --> Node: 200 dropped.
 --> Node: 300 dropped.
 --> Node: 400 dropped.
 --> Node: 500 dropped.
 --> Node: 600 dropped.
-------------------------
List: Second list created.
List: Third list created.
-------------------------
List: Third list dropped.
 --> Node: 60 dropped.
 --> Node: 50 dropped.
 --> Node: 40 dropped.
 --> Node: 30 dropped.
 --> Node: 20 dropped.
 --> Node: 10 dropped.
List: Second list dropped.
 --> Node: 6 dropped.
 --> Node: 5 dropped.
 --> Node: 4 dropped.
 --> Node: 3 dropped.
 --> Node: 2 dropped.
 --> Node: 1 dropped.


*/