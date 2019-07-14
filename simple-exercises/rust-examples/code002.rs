// Creates two hash maps. One that maps an integer to string
// and the other from string to integer.

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


fn main(){

    let (i2c, c2i) = build_hexmap();

    for (i, c) in &i2c {
        println!("{}:{}", i, c);
    }

    for (i, c) in &c2i {
        println!("{}:{}", i, c);
    }
}


/*

3:3
2:2
9:9
11:b
8:8
4:4
6:6
10:a
13:d
0:0
1:1
15:f
7:7
12:c
14:e
5:5
d:13
c:12
4:4
e:14
1:1
b:11
2:2
a:10
3:3
8:8
6:6
9:9
f:15
10:10
0:0
5:5
7:7

*/
