
fn main() {
  let n = 10; 
  let mut v: Vec<u64> = (0..n).collect();
  println!("{:?}", v);
  
 
  //v.iter_mut().for_each(|x| if *x == 4 { *x = 10; });
  
  for x in v.iter_mut() {
      if *x == 4 { *x = 10; };
  }
  
  println!("{:?}", v);
}