use std::net::TcpListener;
use std::io::{Write, Read};

struct RespReader {
    pub buffer: Vec<u8>,
    pub complete: bool,
}

impl RespReader {
    pub fn new() -> Self {
        RespReader { buffer: Vec::new(), complete: false }
    }

    pub fn is_complete(&self) -> bool {
        self.complete
    }

    pub fn add(&mut self, byte_slice: &[u8]) -> Result<(), String> {
        // if start: check if valid + $ : * -
        if self.buffer.len() >= 25 {
            self.buffer.extend(&[13, 10]);
            self.complete = true;
        } else {
            self.buffer.extend(byte_slice);
        }

        Ok(())
    }
}

fn main() {
    let server_addr = "127.0.0.1:6363";
    let listener = TcpListener::bind(server_addr).expect("Did not bind...");
    println!("Listening on: {}", server_addr);

    loop {

        let (mut stream, addr) = listener.accept().expect("did not accept...");
        println!("connection received from {}", addr);

        let mut reader = RespReader::new();

        while !reader.is_complete() {

            let mut buf: Vec<u8> = vec![0; 10]; // TODO: move buffer length to constant

            let length = stream.read(&mut buf)
                .expect("Unable to read from stream...");

            println!("current buf: {:?}", String::from_utf8(buf.clone()).unwrap());

            reader.add(&buf[..length]).expect("Could not add anything..");

            if length < 10 {
                break;
            }
        }

        stream.write("The quick brown fox jumps over the lazy dog".as_bytes())
            .expect("Error writing...");
    }
}

/*


*/
