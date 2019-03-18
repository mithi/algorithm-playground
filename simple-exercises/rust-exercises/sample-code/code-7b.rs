use std::collections::HashMap;

struct Cacher<T> where T: Fn(u32) -> u32 {
  calculate: T, 
  map: HashMap<u32, u32>,
}

impl<T> Cacher<T> where T: Fn(u32) -> u32 {

  fn new(calculate: T) -> Cacher<T> {
    Cacher { calculate, map: HashMap::new() }
  }
  
  fn value(&mut self, i: u32) -> u32 {
    
    if let Some(j) = self.map.get(&i) {
      print!("Cached:");
      return *j;
    }
    
    print!("New:");
    let r = (self.calculate)(i);
    self.map.insert(i, r);
    r
  }
}

fn main() {
  let mut c = Cacher::new(|x| x + 5);
  println!("{}", c.value(1));
  println!("{}", c.value(1));
  println!("{}", c.value(9));
  println!("{}", c.value(9));
}
