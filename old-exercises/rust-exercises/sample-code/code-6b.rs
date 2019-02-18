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
      println!(" > current_link points to node:{} ", boxed_node.element);
     }
    
    while let Some(mut boxed_node) = current_link {
      println!("\nSTART BLOCK. node:{} will be dropped at end.", boxed_node.element);

      current_link =  boxed_node.next.take();

      if let Some(ref this_boxed_node) = current_link {
        // current_link takes ownership from boxed_node.next, boxed_node.next points to None
        println!(" > current_link points to node:{}", this_boxed_node.element);
      }
      println!("END BLOCK.")
    }

    match current_link {
      None => println!(" > Current link points to None"),
      _ => println!("Shouldn't happen"),
    }
    
    println!("\n ...Finally, list: {:?} dropped.", self.name);
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

-------------------------------------------
Dropping list: "First list"... 
 > current_link points to node:100 

START BLOCK. node:100 will be dropped at end.
 > current_link points to node:200
END BLOCK.
 --> node:100 dropped.

START BLOCK. node:200 will be dropped at end.
 > current_link points to node:300
END BLOCK.
 --> node:200 dropped.

START BLOCK. node:300 will be dropped at end.
 > current_link points to node:400
END BLOCK.
 --> node:300 dropped.

START BLOCK. node:400 will be dropped at end.
 > current_link points to node:500
END BLOCK.
 --> node:400 dropped.

START BLOCK. node:500 will be dropped at end.
 > current_link points to node:600
END BLOCK.
 --> node:500 dropped.

START BLOCK. node:600 will be dropped at end.
END BLOCK.
 --> node:600 dropped.
 > Current link points to None

 ...Finally, list: "First list" dropped.
-------------------------------------------
-------------------------------------------
Dropping list: "Third list"... 
 > current_link points to node:60 

START BLOCK. node:60 will be dropped at end.
 > current_link points to node:50
END BLOCK.
 --> node:60 dropped.

START BLOCK. node:50 will be dropped at end.
 > current_link points to node:40
END BLOCK.
 --> node:50 dropped.

START BLOCK. node:40 will be dropped at end.
 > current_link points to node:30
END BLOCK.
 --> node:40 dropped.

START BLOCK. node:30 will be dropped at end.
 > current_link points to node:20
END BLOCK.
 --> node:30 dropped.

START BLOCK. node:20 will be dropped at end.
 > current_link points to node:10
END BLOCK.
 --> node:20 dropped.

START BLOCK. node:10 will be dropped at end.
END BLOCK.
 --> node:10 dropped.
 > Current link points to None

 ...Finally, list: "Third list" dropped.
Dropping list: "Second list"... 
 > current_link points to node:6 

START BLOCK. node:6 will be dropped at end.
 > current_link points to node:5
END BLOCK.
 --> node:6 dropped.

START BLOCK. node:5 will be dropped at end.
 > current_link points to node:4
END BLOCK.
 --> node:5 dropped.

START BLOCK. node:4 will be dropped at end.
 > current_link points to node:3
END BLOCK.
 --> node:4 dropped.

START BLOCK. node:3 will be dropped at end.
 > current_link points to node:2
END BLOCK.
 --> node:3 dropped.

START BLOCK. node:2 will be dropped at end.
 > current_link points to node:1
END BLOCK.
 --> node:2 dropped.

START BLOCK. node:1 will be dropped at end.
END BLOCK.
 --> node:1 dropped.
 > Current link points to None

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
