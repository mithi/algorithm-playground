#[derive(Debug, Clone)]
pub struct MockStream {
    pub message: Vec<u8>,
    pub current: usize,
}



impl MockStream {
    pub fn new(m: &str) -> Self {

        MockStream { message: m.to_string().into_bytes(), current: 0 }
    }

    pub fn next(&mut self) -> u8 {

        if self.current < self.message.len() {
            self.current += 1;
            self.message[self.current - 1].clone()
        } else {
            0
        }
    }
}

#[cfg(test)]
mod test {
    use super::*;

    #[test]
    pub fn new() {
        let mock_stream = MockStream::new("Hello");
        assert_eq!(mock_stream.message, vec![72, 101, 108, 108, 111]);
        assert_eq!(mock_stream.current, 0);
    }


    #[test]
    pub fn next() {
        let mut mock_stream = MockStream::new("Hello");
        assert_eq!(mock_stream.next(), "H".to_string().into_bytes()[0]);
        assert_eq!(mock_stream.next(), "e".to_string().into_bytes()[0]);
        assert_eq!(mock_stream.next(), "l".to_string().into_bytes()[0]);
        assert_eq!(mock_stream.next(), "l".to_string().into_bytes()[0]);
        assert_eq!(mock_stream.next(), "o".to_string().into_bytes()[0]);
        assert_eq!(mock_stream.next(), 0);
        assert_eq!(mock_stream.next(), 0);

    }

}
