extern crate sorting;

use sorting::selection;
use sorting::insertion;


fn main() {

    println!("Selection Sort");
    
    let mut v = vec![9.0, 8.0, 6.0, 7.0, 1.0, 2.0, 4.0, 3.0, 5.0];
    println!("start: {:?}", v);

    selection::sort(&mut v);
    println!("end: {:?}", v);

    let mut v = vec!["apple", "carrot", "banana", "deer", "d"];
    println!("start: {:?}", v);

    selection::sort(&mut v);
    println!("end: {:?}", v);

    println!("Insertion Sort");
    
    let mut v = vec![9.0, 8.0, 6.0, 7.0, 1.0, 2.0, 4.0, 3.0, 5.0];
    println!("start: {:?}", v);

    insertion::sort(&mut v);
    println!("end: {:?}", v);

    let mut v = vec!["apple", "carrot", "banana", "deer", "d"];
    println!("start: {:?}", v);

    insertion::sort(&mut v);
    println!("end: {:?}", v);

}

