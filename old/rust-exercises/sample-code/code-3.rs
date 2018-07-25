// Run in https://play.rust-lang.org/
// Implement generic `get_minimum()` function of vector

use std::fmt::Display;

enum SomethingOrNothing <T> {
  Something(T),
  Nothing,
}

impl<T> SomethingOrNothing<T> where T: Display + Clone {
  
  fn print(&self) {
    match self {
      SomethingOrNothing::Something(t) => println!("I have `{}`.", t),
      _ => println!("I have nothing."),
    };
  }
}


fn min<'a, T: PartialOrd>(x: &'a T, y: &'a T) -> &'a T {
  if x < y { x } else { y }
}


fn get_minimum<T>(v: &[T]) -> SomethingOrNothing<T> where T: PartialOrd + Clone { 

  fn has_elements_minimum<T: PartialOrd + Clone>(v: &[T]) -> T {
    let mut n = &v[0];
    for x in &v[1..] { n = min(n, x); }
    n.clone()
  }

  match v.len() {
    0 => SomethingOrNothing::Nothing,
    _ => SomethingOrNothing::Something(has_elements_minimum(&v)),
  }
}


fn main() {

  let x = vec!["carrot", "apple", "banana"];
  let y = vec!['b', 'd', 'a', 'c'];
  let z = vec![24, 20, 30, 15, 31, 32];
  let w = vec![-1.0, -2.25, 10.25, 5.0, 2.0, 1.0];
  let v = Vec::<i32>::new();
  
  get_minimum(&x).print(); // I have `apple`.
  get_minimum(&y).print(); // I have `a`.
  get_minimum(&z).print(); // I have `15`.
  get_minimum(&w).print(); // I have `-2.25`.
  get_minimum(&v).print(); // I have nothing.
}
