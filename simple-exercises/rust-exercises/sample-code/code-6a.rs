use std::mem;
type Link = Option<Box<Node>>;

struct List {
  head: Link,
  name: String,
}

#[derive(Debug)]
struct Node {
  element: i32,
  next: Link,
}

impl List {

  fn new(given_name: &str) -> Self {
    println!("List: {} created.", given_name);
    List { head: None, name: String::from(given_name) }
  }

  fn push(&mut self, i: i32) {

    let old_head = self.head.take();    
    let new_node = Node { element: i, next: old_head };
    self.head = Some(Box::new(new_node));
  }
}

impl Drop for Node {
  fn drop(&mut self) {
    println!(" --> node:{} dropped.", self.element);
  }
}

impl Drop for List {

  fn drop(&mut self) {

    println!("Dropping list: {:?}... ", self.name);
    
    let mut current_link = self.head.take();

    if let Some(ref boxed_node) = current_link {
      println!(" > current_link: node:{} ", boxed_node.element);
     }
    
    while let Some(mut boxed_node) = current_link {
      current_link =  boxed_node.next.take();

      if let Some(ref this_boxed_node) = current_link {
        // current_link takes ownership from boxed_node.next, boxed_node.next points to None
        println!(" > current_link: node:{}", this_boxed_node.element);
      }
    }

    match current_link {
      None => println!(" > Current link: None"),
      _ => println!("Shouldn't happen"),
    }
    
    println!("...Finally, list: {:?} dropped.", self.name);
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
  
  println!("-------------------------------------------");
  mem::drop(a);
  
  println!("-------------------------------------------");
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
  
  println!("-------------------------------------------");
}

/* 
List: First list created.
-------------------------------------------
Dropping list: "First list"... 
 > current_link: node:100 
 > current_link: node:200
 --> node:100 dropped.
 > current_link: node:300
 --> node:200 dropped.
 > current_link: node:400
 --> node:300 dropped.
 > current_link: node:500
 --> node:400 dropped.
 > current_link: node:600
 --> node:500 dropped.
 --> node:600 dropped.
 > Current link: None
...Finally, list: "First list" dropped.
-------------------------------------------
List: Second list created.
List: Third list created.
-------------------------------------------
Dropping list: "Third list"... 
 > current_link: node:60 
 > current_link: node:50
 --> node:60 dropped.
 > current_link: node:40
 --> node:50 dropped.
 > current_link: node:30
 --> node:40 dropped.
 > current_link: node:20
 --> node:30 dropped.
 > current_link: node:10
 --> node:20 dropped.
 --> node:10 dropped.
 > Current link: None
...Finally, list: "Third list" dropped.
Dropping list: "Second list"... 
 > current_link: node:6 
 > current_link: node:5
 --> node:6 dropped.
 > current_link: node:4
 --> node:5 dropped.
 > current_link: node:3
 --> node:4 dropped.
 > current_link: node:2
 --> node:3 dropped.
 > current_link: node:1
 --> node:2 dropped.
 --> node:1 dropped.
 > Current link: None
...Finally, list: "Second list" dropped.

------------
NOTES
------------

Because of deref coercion / autodereferencing the following are equivalent:
- boxed_node.element and (*boxed_node).element
- boxed_node.next and (*box_node).next 

let z = mem::replace(&mut x, val);
- z will point at object that x used to point at
- x will now point at val  

let y = x.take();
- x now points to None
- y now points to where x used to point 

*/
