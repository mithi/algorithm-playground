type Link<T> = Option<Box<Node<T>>>;

pub struct IntoIter<T>(List<T>);

pub struct Iter<'a, T: 'a> { 
  next: Option<&'a Node<T>> 
}

pub fn new_link<T>(node: Node<T>) -> Link<T> {
  Some(Box::new(node))
}

pub struct Node<T> {
  element: T, 
  next: Link<T>,
}

pub struct List<T> {
  head: Link<T>,
  name: String,
  count: u32,
}


impl<T> Node<T>{

  fn new(element: T, next: Link<T>) -> Self {
    Node { element,  next }
  } 
}

impl <'a, T> List<T> {

  pub fn new(name: String) -> Self {
    List { head: None, name, count: 0 }
  }

  pub fn push(&mut self, i: T) {
    let node = Node::new(i, self.head.take());
    self.head = new_link(node);
    self.count += 1;
  }
  
  pub fn pop(&mut self) -> Option<T> {
    
    self.head.take().map(|boxed_node| {
      let node = *boxed_node;
      self.head = node.next;
      self.count -= 1;
      node.element
    })
  }

  pub fn peek(&self) -> Option<&T> {
    self.head.as_ref().map(|b| &b.element)
  }

  pub fn into_iter(self) -> IntoIter<T> {
    IntoIter(self)
  }

  pub fn iter(&'a self) -> Iter<'a, T> {
    Iter { next: self.head.as_ref().map(|b| &**b) }
  }
}

impl<T> Iterator for IntoIter<T> {
  type Item = T;
  fn next(&mut self) -> Option<Self::Item> {
    self.0.pop()
  }
}


impl<'a, T> Iterator for Iter<'a, T> {
  type Item = &'a T; 
  fn next(&mut self) -> Option<Self::Item> {
    self.next.map(|node| {
      self.next = node.next.as_ref().map(|b| &**b);
      &node.element
    })
  }
}


impl<T> Drop for List<T> {
  // Drop nodes iteratively instead of recursively by default
  fn drop(&mut self) {
    let mut current_link = self.head.take();
    while let Some(mut boxed_node) = current_link {
      current_link = boxed_node.next.take() // (*boxed_noode).next
    }
    println!("List {} dropped.", self.name);
  }
}

#[cfg(test)]
mod test {
  use super::*;
  
  #[test]
  pub fn test_peek() {
    let mut a = List::new(String::from("First List"));
    assert_eq!(a.peek(), None);
    assert_eq!(a.count, 0);

    a.push(vec![1, 2]);
    assert_eq!(a.peek(), Some(&vec![1, 2]));
    assert_eq!(a.count, 1);

    a.push(vec![2, 3, 4]);
    assert_eq!(a.peek(), Some(&vec![2, 3, 4]));
    assert_eq!(a.count, 2);

    assert_eq!(a.peek(), Some(&vec![2, 3, 4]));
    assert_eq!(a.count, 2);
  }

  #[test]
  pub fn test_push_pop_string() {
    let mut a = List::new(String::from("First List"));

    assert_eq!(a.name, String::from("First List"));
    assert_eq!(a.count, 0);
    assert_eq!(a.pop(), None);
    assert_eq!(a.count, 0);

    a.push(String::from("Hi"));
    assert_eq!(a.count, 1);
    a.push(String::from("World,"));
    assert_eq!(a.count, 2);
    a.push(String::from("Hello"));
    assert_eq!(a.count, 3);
    a.push(String::from("Rust!"));
    assert_eq!(a.count, 4);

    assert_eq!(a.pop(), Some(String::from("Rust!")));
    assert_eq!(a.count, 3);
    assert_eq!(a.pop(), Some(String::from("Hello")));
    assert_eq!(a.count, 2);
    assert_eq!(a.pop(), Some(String::from("World,")));
    assert_eq!(a.count, 1);
    assert_eq!(a.pop(), Some(String::from("Hi")));
    assert_eq!(a.count, 0);
    assert_eq!(a.pop(), None);
    assert_eq!(a.count, 0);

  }

  #[test]
  pub fn test_node() {

    let n = Node::new(String::from("Hello"), None);
    assert!(n.element == "Hello".to_string());

    let n = Node::new('a',  None);
    assert!(n.element == 'a');

    let n = Node::new(32,  None);
    assert!(n.element == 32);

    let n = Node::new(6.25,  None);
    assert!(n.element == 6.25);

    let n = Node::new(vec![1, 2, 3],  None);
    assert!(n.element == vec![1, 2, 3]);

  }
 
  fn validate_element<T>(link: &Link<T>, element: T) -> bool 
    where T: PartialEq {

    if let Some(ref boxed_node) = link {
      return boxed_node.element == element;
    }
    false 
  }

  #[test]
  pub fn test_link() {
    
    let n = Node::new(String::from("Hello"), None);
    let m = Node::new(String::from("World"), new_link(n));    
    let b = validate_element(&m.next, "Hello".to_string());
    assert!(b);

    let n = Node::new('a', None);
    let m = Node::new('b', new_link(n));
    let b = validate_element(&m.next, 'a');
    assert!(b);

    let n = Node::new(32, None);
    let m = Node::new(20, new_link(n));
    let b = validate_element(&m.next, 32);
    assert!(b);

    let n = Node::new(6.25, None);
    let m = Node::new(11.0, new_link(n));
    let b = validate_element(&m.next, 6.25);
    assert!(b);

    let n = Node::new(vec![1, 2, 3], None);
    let m = Node::new(vec![1, 4, 3], new_link(n));
    let b = validate_element(&m.next, vec![1, 2, 3]);
    assert!(b);
  }

}


/*

NOTES: 

-------------------------
pop()
-------------------------
If head is None, return None.
else head is Some(Box(Node(Element, Next: LINK)))
Unwrap Some -> Box
Unwrap Box -> Node
Unwrap Node -> element: T, Next: LINK
point head to the next: LINK
return Some(element)

-------------------------
type alias can't have functions
-------------------------

https://stackoverflow.com/questions/35568871/
is-it-possible-to-implement-inherent-methods-on-type-aliases

A: Not really. A type alias (type Foo = Bar) does not create a new type. 
All it does is create a different name that refers to the existing type.
In Rust, you are not allowed to implement inherent methods for a type that
comes from another crate.

-------------------------
map() Function: 
-------------------------

a.map(|i| f(i)) where a is of type Option
if a = Some(i), return Some(f(i))
if a = None, return None

----------------------
as_ref() and as_mut()
----------------------
self.head.as_ref().map(|b| (&b.element)) 

map takes self by value, which moves variable out
use as_ref(), return a reference to node element instead
since we just want to take a "peek", no need to clone
use as_mut() if you want to return a mutable reference
&b 

----------------------
&boxed_node.element == &(*boxed_node).element
----------------------
because of deref coercion

----------------------
Iterator IntoIter and Iter
----------------------
IntoIter
Takes ownership of List
consumes each Option<T> each time you call next

Iter
Returns borrowed references 
to each link of list for each `next()`

*/