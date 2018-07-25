use std::io::prelude::*;
use std::net::TcpStream;

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
        // if + > read until crlf
        // if - > read until crlf
        // if : > read until crlf
        // if $ > get n by reading until crlf, then get next n bytes, check if next 2 bytes is crlf
        // if * > get n by reading until crlf, for i in 0..n
        //
        if self.buffer.len() == 0
        match

        Ok(())
    }
}

pub fn get_response(query: &[u8]) -> Result<Vec<u8>, String> {

    let mut stream = TcpStream::connect("127.0.0.1:6363")
        .expect("Couldn't connect to the server...");

    stream.write_all(query)
        .expect("Could not write...");

    let mut reader = RespReader::new();

    while !reader.is_complete() {

        let mut buf: Vec<u8> = vec![0; 10]; // TODO: move buffer length to constant

        let length = stream.read(&mut buf)
            .expect("Unable to read from stream...");

        println!("current buf: {:?}", String::from_utf8(buf.clone()).unwrap());

        if reader.add(&buf[..length]).is_err() {
            return Err("Server sent weird data".to_string());
        }
    }

    return Ok(reader.buffer)
}


