pub mod mockstream;
pub mod respreader;
pub use mockstream::MockStream;

pub struct RespWriter;

impl RespWriter {

    pub fn to_simple_string(s: &str) -> Result<String, String> {
        RespWriter::to_simple_message("+", s)
    }

    pub fn to_error(s: &str) -> Result<String, String> {
        RespWriter::to_simple_message("-", s)
    }

    pub fn to_simple_message(prefix: &str, s: &str) -> Result<String, String> {

        if s.contains("\r\n") {
            return Err("Contains crlf".to_string());
        }

        let m = format!("{}{}\r\n", prefix, s);
        Ok(m)
    }

    pub fn to_integer(i: usize) -> String {
        format!(":{}\r\n", i)
    }

    pub fn to_bulk_string(s: &str) -> String {
        format!("${}\r\n{}\r\n", s.len(), s)
    }

    pub fn null_bulk_string() -> String {
        "$-1\r\n".to_string()
    }
}


#[cfg(test)]
mod test {

    use super::RespWriter;

    #[test]
    pub fn check_simple_string() {
        assert_eq!("+OK\r\n", RespWriter::to_simple_string("OK").unwrap());
        assert!(RespWriter::to_simple_string("PING\r\n...").is_err());
    }

    #[test]
    pub fn check_simple_error() {
        assert_eq!("-ERR\r\n", RespWriter::to_error("ERR").unwrap());
        assert!(RespWriter::to_error("PONG\r\n...").is_err());
    }

    #[test]
    pub fn check_integer() {
        assert_eq!(":100\r\n", RespWriter::to_integer(100));
    }

    #[test]
    pub fn check_bulk_string() {
        assert_eq!("$0\r\n\r\n", RespWriter::to_bulk_string(""));
        assert_eq!("$6\r\nfoobar\r\n", RespWriter::to_bulk_string("foobar"));
        assert_eq!("$2\r\n\r\n\r\n", RespWriter::to_bulk_string("\r\n"));
        assert_eq!("$4\r\n😍\r\n", RespWriter::to_bulk_string("😍"));
    }

    #[test]
    pub fn check_null_bulk_string() {
        assert_eq!("$-1\r\n", RespWriter::null_bulk_string());
    }
}
