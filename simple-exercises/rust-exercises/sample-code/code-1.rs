// Run in https://play.rust-lang.org/
// Get minimum value in an i32 vec

enum NumberOrNothing {
  Number(i32),
  Nothing,
}

impl NumberOrNothing {
  fn print(&self) {
    match self {
      NumberOrNothing::Nothing => println!("No number (Nothing)"),
      NumberOrNothing::Number(n) => println!("Number is {}", n),
    };
  }
}


fn min(a: i32, b: i32) -> i32 {
  if a < b { a } else { b }
}


fn get_minimum(vec: &[i32]) -> NumberOrNothing { 

  fn has_elements_minimum(vec: &[i32]) -> i32 {
    let mut n = vec[0];
    for x in & vec[1..]{ n = min(n, *x); }
    n
  }
  
  match vec.len() {
    0 => NumberOrNothing::Nothing,
    _ => NumberOrNothing::Number(has_elements_minimum(&vec)),
  }
}


fn main() {

  let mut v = vec![18, 5, 7, 1, 27];
  let mut w: std::vec::Vec<i32> = Vec::new();
  
  get_minimum(&v).print(); // Number is 1 
  get_minimum(&w).print(); // No number (nothing)
  
  v.push(-1);
  get_minimum(&v).print(); // Number is -1
  
  w.push(100);
  get_minimum(&w).print(); // Number is 100
}
