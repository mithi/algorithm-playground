extern crate sorting;
use sorting::shuffle;

fn main() {

    println!("\n --------------- \n Shuffle \n --------------- \n");
    let mut array: Vec<usize> = (0..30).collect();

    println!("\nstart: {:?}", array);
    shuffle(&mut array);
    println!("end: {:?} \n", array);
}

