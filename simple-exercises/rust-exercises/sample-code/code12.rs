

fn main() {
  let v = " hello \n world hehe \n hi rust \n no rust";
  let mut lines = v.lines();
  
  
  lines.by_ref()
       .take_while(|line| !line.contains("world"))
       .for_each(|line| println!("{}", line));

  lines.for_each(|line| println!("{}", line));
}

/*

hello 
hi rust 
no rust

*/

