extern crate sorting;

use sorting::selection;
use sorting::insertion;
use sorting::shell;
use sorting::merge;
use sorting::shuffle;
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

    let v_sample = vec![62, 83, 18, 53, 7, 17, 95, 86, 47, 69, 25, 28];
    let v_float: Vec<_> = (0..30).rev().map(|i| i as f64).collect();
    let v_string = vec!["apple", "carrot", "banana", "deer", "d", "zebra"];
    let v_int: Vec<usize> = (0..20).collect();


    println!("\n --------------- \n Selection Sort \n --------------- \n");
    display_sort(&v_sample, selection::sort);
    display_sort(&v_float, selection::sort);
    display_sort(&v_string, selection::sort);
    display_sort(&v_int, selection::sort);

    println!("\n --------------- \n Insertion Sort \n --------------- \n");
    display_sort(&v_sample, insertion::sort);
    display_sort(&v_float, insertion::sort);
    display_sort(&v_string, insertion::sort);
    display_sort(&v_int, insertion::sort);

    println!("\n --------------- \n Shell Sort \n --------------- \n");

    let gaps = vec![5, 3, 1];
    let mut array = v_sample.clone();

    println!("\nstart: {:?}", array);
    shell::sort(&mut array, &gaps);
    println!("end: {:?} \n", array);


    let gaps = vec![701, 301, 132, 57, 23, 10, 4, 1];
    let mut array: Vec<_> = (0..30).rev().collect();

    println!("\nstart: {:?}", array);
    shell::sort(&mut array, &gaps);
    println!("end: {:?} \n", array);

    println!("\n --------------- \n Merge Sort \n --------------- \n");

    let mut array: Vec<usize> = vec![8, 29, 15, 22, 23, 30, 16, 9, 11, 25, 14, 18, 28, 4, 7, 21, 23];
    println!("\nstart: {:?}", array);
    merge::sort(&mut array);
    println!("end: {:?} \n", array);

    println!("\n --------------- \n Shuffle \n --------------- \n");
    let mut array: Vec<usize> = (0..30).collect();

    println!("\nstart: {:?}", array);
    shuffle(&mut array);
    println!("end: {:?} \n", array);

    let mut array = v_string.clone();
    println!("\nstart: {:?}", array);
    shuffle(&mut array);
    println!("end: {:?} \n", array);
}

