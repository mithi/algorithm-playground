fn main() {
    
  let (a, b, c) = (&mut [1], &mut [2], &mut [3]);
  let v: Vec<&mut [u8]> = vec![a, b, c];
  let (x, y, z) = (&mut [1, 2], &mut [2, 3], &mut [3, 4]);
  let w: Vec<&mut [u8]> = vec![x, y, z];

  println!("{:?}", v);
  println!("{:?}", w);
    
  // &str "hello", &String::from("hello")[..], &String::from("hello")
    
  let m = [1, 2, 3];
  let n = vec![4, 5, 6];
  test(&n);
  test(&m);
    
  let h = [9, 8, 7, 6, 5, 4];
  let j: Vec<&[u8]> = h.chunks(2).collect();
  println!("{:?}", j);
}

fn test(list: &[u8]) {
  println!("{:?}", list);
}

/*

[[1], [2], [3]]
[[1, 2], [2, 3], [3, 4]]
[4, 5, 6]
[1, 2, 3]
[[9, 8], [7, 6], [5, 4]]

*/