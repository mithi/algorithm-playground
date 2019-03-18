// Run in https://play.rust-lang.org/
// Implement generic enum `SomethingOrNothing`

use std::fmt::Display;

enum SomethingOrNothing <T> {
    Something(T),
    Nothing,
}

impl<T> SomethingOrNothing<T> 
  where T: Display + Clone {
  
  fn new(t: Vec<T>) -> Self {
    match t.len() {
      0 => SomethingOrNothing::Nothing,
      i if i == 1 => SomethingOrNothing::Something(t[0].clone()),
      _ => panic!("Expecting `Vec` of length one or zero"),
    } 
  }

  fn print(&self) {
    match self {
      SomethingOrNothing::Something(t) => println!("I have `{}`.", t),
      _ => println!("I have nothing."),
    };
  }
}

fn main() {
  let v = SomethingOrNothing::new(Vec::<i32>::new());
  let w = SomethingOrNothing::new(vec!["hello"]);
  let x = SomethingOrNothing::new(vec![41]);

  v.print(); // I have nothing.
  w.print(); // I have `hello`.
  x.print(); // I have `41`.
  
  // let y = SomethingOrNothing::new(vec![41, 23]); 
  // Uncomment line above, you'll get:
  // thread 'main' panicked at 'Expecting `Vec` of length one or zero'
}