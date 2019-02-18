struct Calc<T> where T: Fn(i32) -> i32 {
  f: T
}

impl<T> Calc<T> where T: Fn(i32) -> i32 {

  fn new(f: T) -> Calc<T> {
    Calc{ f }
  }
  
  fn value(&self, i: i32) -> i32 {
    (self.f)(i) // f(i) will return error "field, not a method"
  }
}

fn main() {

  let c = Calc::new(|x| x + 1);
  println!("{}", c.value(4)); // 5
  
  let new_f = |x| x * 2 ; 
  let d = Calc::new(new_f);
  println!("{}", d.value(6)); // 12
  
  let another_f = |x| x + 3;
  println!("{}", another_f(10)); // 13
  println!("{}", (another_f)(10)); // 13

}