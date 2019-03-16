// given a reference to an even-lengthed ascii string
// print two characters at a time

fn print_two(x: &char, y: &char) {
    println!("{} {}", x, y)
}


fn main() {

    let x: &str = "abcdef1234567890";

    assert!(x.is_ascii());
    assert_eq!(0, x.len() % 2);

    let mut i = 0;

    loop {
        let a = x.chars().nth(i).unwrap();
        let b = x.chars().nth(i + 1).unwrap();
        print_two(&a, &b);
        if i + 2 == x.len() {
            break;
        }
        i += 2;
    }

    // a b
    // c d
    // e f
    // 1 2
    // 3 4
    // 5 6
    // 7 8
    // 9 0
}
