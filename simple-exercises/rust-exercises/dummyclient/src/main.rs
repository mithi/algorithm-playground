extern crate dummyclient;
use dummyclient::MockStream;
use dummyclient::respreader::get_response;

fn main() {
    example();

// set(key, value)
// delete(key)
// get(key)
// exist(key)

}


/*

start of message
*

*/

fn example() {
    //println!("Hello, world!");

    //let mock_stream = MockStream::new("Hello!");
    //println!("{:?}", mock_stream);
    //MockStream { message: [72, 101, 108, 108, 111], current: 0 }

    let x = get_response(&"hello world! nice to meet you! :) ".to_string().into_bytes());
    println!("response: {:?}", String::from_utf8(x.clone().unwrap()));

    let x = get_response(&"joseph michael galero".to_string().into_bytes());
    println!("response: {:?}", String::from_utf8(x.clone().unwrap()));

}
