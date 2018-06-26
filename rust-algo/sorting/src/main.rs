extern crate sorting;

use sorting::selection;
use sorting::insertion;
use std::fmt::Debug;

fn display_sort<T, F>(x: &[T], sort: F) 
  where T: PartialOrd + Debug + Clone, 
        F: Fn(&mut [T]) {

  println!("\nstart: {:?}", x);

  let mut v = x.to_vec();
  sort(&mut v);

  println!("end: {:?} \n", v);
}


fn main() {
    
    let v_float = vec![9.0, 8.0, 6.0, 7.0, 1.0, 2.0, 4.0, 3.0, 5.0];
    let v_string = vec!["apple", "carrot", "banana", "deer", "d"];
    let v_int = vec![1, 2, 3, 4, 5];

    println!("\n --------------- \n Selection Sort \n --------------- \n");
    display_sort(&v_float, selection::sort);
    display_sort(&v_string, selection::sort);
    display_sort(&v_int, selection::sort);    

    println!("\n --------------- \n Insertion Sort \n --------------- \n");
    display_sort(&v_float, insertion::sort);
    display_sort(&v_string, insertion::sort);    
    display_sort(&v_int, insertion::sort);    

}

