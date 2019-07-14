// A very convoluted way to convert a hex string to sa vector of bytes and back

use std::collections::HashMap;

fn build_hexmap() -> (HashMap<u8, String>, HashMap<String, u8>) {

    let mut i2c = HashMap::new();
    let mut c2i = HashMap::new();

    let chars = ["a", "b", "c", "d", "e", "f"];

    for i in 0..=10 {
        i2c.insert(i as u8, i.to_string());
        c2i.insert(i.to_string(), i as u8);
    }

    for i in 10..16 {
        let j = chars[i - 10].to_string();
        i2c.insert(i as u8, j.clone());
        c2i.insert(j, i as u8);
    }

    (i2c, c2i)
}


#[derive(Debug, Clone)]
pub struct HexConverter {
    i2c: HashMap<u8, String>,
    c2i: HashMap<String, u8>,
}


impl HexConverter {

    pub fn new() -> Self {
        let (i2c, c2i) = build_hexmap();
        HexConverter { i2c, c2i }
    }

    pub fn to_byte(&self, s: &str) -> Option<u8> {

        assert!(s.is_ascii());
        assert_eq!(2, s.len());

        let a = &s[0..1];
        let b = &s[1..2];
        if let (Some(x), Some(y)) = (self.c2i.get(a), self.c2i.get(b)) {
            Some(16 * x + y)
        } else {
            None
        }
    }

    pub fn from_byte(&self, u: u8) -> String {

        let a = u / 16;
        let x = self.i2c.get(&a).unwrap();
        let b = (u - 16 * a) % 16;
        let y = self.i2c.get(&b).unwrap();
        format!("{}{}", x, y)
    }

    pub fn from_bytes(&self, v: &[u8]) -> String {
        let mut s = String::new();
        for i in v {
            s.push_str(&self.from_byte(*i));
        }
        s
    }

    pub fn to_bytes(&self, s: &str) -> Option<Vec<u8>> {

        assert!(s.is_ascii());
        assert_eq!(0, s.len() % 2);

        let x = s.len() / 2;
        let mut v = Vec::new();

        for i in 0..x {
            let (j, k) = (2 * i, 2 * i + 2);
            if let Some(a) = self.to_byte(&s[j..k]) {
                v.push(a);
            } else { return None }
        }
        Some(v)
    }
}


fn main(){

    let h = HexConverter::new();

    println!("{}", h.to_byte("fe").unwrap()); // 254
    println!("{}", h.from_byte(254)); // fe

    println!("{:?}", h.to_bytes("ff2afd").unwrap()); // [255, 42, 253]
    println!("{}", h.from_bytes(&vec![47, 179, 205])); // 2fb3cd
}
