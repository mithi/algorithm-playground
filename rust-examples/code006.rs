// convert string in base 64 to vector of u8
// https://docs.rs/crate/base64/0.3.1/source/tests/tests.rs

#[macro_use]
extern crate lazy_static;
use std::collections::HashMap;

const ALL64: [char; 64] = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
        'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
        '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/'
    ];


lazy_static! {
    static ref MAP64: HashMap<char, usize> = {
        let mut m = HashMap::new();
        for i in 0..64 {
            m.insert(ALL64[i], i);
        }
        m
    };
}

fn push_three(v: &mut Vec<u8>, r: usize) {
    let mask = 255;
    let (a, b, c) = ((r >> 16) & mask, (r >> 8) & mask, r & mask);
    v.push(a as u8);
    v.push(b as u8);
    v.push(c as u8);
}

fn get64(x: &Option<char>) -> usize {
    *MAP64.get(&x.unwrap()).unwrap()
}

fn from_base64(s: &str) -> Vec<u8> {
    let mut v = Vec::new();
    let l = s.len() / 4 - 1;
    let mut chars = s.chars();
    let mask = 255;

    for _ in 0..l {
        let mut r = 0;
        for _ in 0..4 {
            //let x = MAP64.get(&(chars).next().unwrap()).unwrap();
            r = (r << 6) + get64(&chars.next());
        }
        push_three(&mut v, r);
    }

    let x = get64(&chars.next());
    let y = get64(&chars.next());

    let mut r = (x  << 18) + (y << 12);

    let a = (chars).next().unwrap_or('=');
    let b = (chars).next().unwrap_or('=');

    if a != '=' {
        let a = MAP64.get(&a).unwrap();
        r = r + (a << 6);

        if b != '=' {
            let b = MAP64.get(&b).unwrap();
            r = r + b;
            push_three(&mut v, r);
        } else {
            v.push((r >> 16 & mask) as u8);
            v.push((r >> 8 & mask) as u8);
        }
    } else {
        assert_eq!('=', b);
        v.push((r >> 16) as u8);
    }
    v
}


fn main() {

    let s = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t";
    let t = "TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4=";
    let v = from_base64(&s);
    let w: Vec<u8> = vec![
        73, 39, 109, 32, 107, 105, 108, 108, 105, 110, 103, 32, 121, 111, 117, 114,
        32, 98, 114, 97, 105, 110, 32, 108, 105, 107, 101, 32, 97, 32, 112, 111, 105,
        115, 111, 110, 111, 117, 115, 32, 109, 117, 115, 104, 114, 111, 111, 109
        ];

    assert_eq!(v, w);

    println!("{:?}", String::from_utf8(from_base64("VGVzdAo=")).unwrap()); // Test\n
    println!("{:?}", String::from_utf8(from_base64(&t)).unwrap());
    println!("{:?}", String::from_utf8(from_base64("YW55IGNhcm5hbCBwbGVhc3VyZS4=")).unwrap()); //any carnal pleasure.
    println!("{:?}", String::from_utf8(from_base64("YW55IGNhcm5hbCBwbGVhc3VyZQ==")).unwrap()); //any carnal pleasure
    println!("{:?}", String::from_utf8(from_base64("YW55IGNhcm5hbCBwbGVhcw==")).unwrap()); //any carnal pleas
}
