
// A better way to convert a hex string to vec of u8 and back
use std::char;

fn from_hex(s: &str) -> Option<Vec<u8>>{

    assert_eq!(0, s.len() % 2);

    let okv: Result<Vec<u8>, _> = (0..s.len())
        .step_by(2)
        .map(|i| u8::from_str_radix(&s[i..i+2], 16))
        .collect();

    if let Ok(v) = okv {
        Some(v)
    } else {
        None
    }
}

fn to_hex(v: &[u8]) -> String {
    let mut s = String::new();
    for i in v {
        let x = i / 16;
        let y = i % 16;
        let a = char::from_digit(x as u32, 16).unwrap();
        let b = char::from_digit(y as u32, 16).unwrap();
        s.push(a);
        s.push(b)
    }
    s
}

fn main(){

    let s = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
    let x = from_hex(s).unwrap();
    println!("{:?}", x);
    let y = to_hex(&x);
    println!("{:?}", &y);
    assert_eq!(s, &y);
    // [73, 39, 109, 32, 107, 105, 108, 108, 105, 110, 103, 32, 121, 111, 117, 114, 32, 98, 114, 97, 105, 110, 32, 108, 105, 107, 101, 32, 97, 32, 112, 111, 105, 115, 111, 110, 111, 117, 115, 32, 109, 117, 115, 104, 114, 111, 111, 109]
    //"49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

}




