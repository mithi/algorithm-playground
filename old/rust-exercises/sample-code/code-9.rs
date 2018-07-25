type Link<T> = Option<Box<Node<T>>>;

pub struct List<T> {
  head: Link<T>,
  name: String,
  count: i32,
}

struct Node<T> {
  element: T,
  next: Link<T>,
}

impl<'a, T> List<T> {
  pub fn new(name_given: &str) -> Self {
    List { head: None, name: String::from(name_given), count: 0}
  }

  pub fn push(&mut self, i: T) {
    let node = Node {element: i, next: self.head.take() };
    self.head = Some(Box::new(node));
    self.count += 1;
  }

  pub fn pop(&mut self) -> Option<T> {
    // a.map(|i| f(i)), where a = Some(i), return Some(f(i))
    // if a = None, return None
    self.head.take().map(|boxed_node| {
      let node = *boxed_node;
      self.head = node.next;
      self.count -= 1;
      node.element
    })
  }

  pub fn peek(&self) -> Option<&T> {
    // map takes self by value, which moves variable out
    // use as_ref(), return a reference to node element instead
    // since we just want to take a "peek", no need to clone
    // use as_mut() if you want to pass a mutable reference
    self.head.as_ref().map(|b| (&b.element)) 
  }

  pub fn into_iter(self) -> IntoIter<T> {
    IntoIter(self)
  }

  pub fn iter(&'a self) -> Iter<'a, T> {
    Iter { next: self.head.as_ref().map(|b| &**b) }
  }
}

// Takes ownership of List
// consumes each Option<T> each time you call next
pub struct IntoIter<T>(List<T>);

// Returns borrowed references 
// to each link of list for each `next()`
pub struct Iter<'a, T: 'a> {
    next: Option<&'a Node<T>>,
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

fn main() {
  let mut a = List::new("hello");
  a.push(1);
  a.push(2);
  println!("{:?}", a.peek());
  println!("{:?}", a.peek());
  println!("{:?}", a.pop());
  println!("{:?}", a.peek());
  println!("{:?}", a.pop());
  println!("{:?}", a.peek());
  println!("{:?}", a.pop());
  println!("{:?}", a.peek());

  let mut list = List::new("second list!");
  list.push(1); list.push(2); list.push(3);

  let mut iter = list.into_iter();
  assert_eq!(iter.next(), Some(3));
  assert_eq!(iter.next(), Some(2));
  assert_eq!(iter.next(), Some(1));
  assert_eq!(iter.next(), None);
  assert_eq!(iter.next(), None);
}