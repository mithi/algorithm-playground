use super::shuffle;
use rand::{thread_rng, Rng};

pub fn numbers(n: usize, m: usize) -> Vec<usize> {
    let mut rng = thread_rng();
    let mut v = Vec::new();
    for _ in 0..n {
        let r = rng.gen_range(0, m);
        v.push(r);
    }
    v
}


pub fn random_strings(n: usize) -> Vec<String> {

    let x = "abcdefghijklmnabcd".to_string().into_bytes();
    let mut v = Vec::new();

    for _ in 0..n {
        let mut s = x.clone();
        shuffle(&mut s);
        let n = String::from_utf8(s).unwrap().clone();
        v.push(n);
    }
    v
}

