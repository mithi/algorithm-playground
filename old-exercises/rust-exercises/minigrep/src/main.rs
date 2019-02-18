extern crate minigrep;

use std::env;
use std::process;
use minigrep::Config;

fn main() {
  
  let config = Config::new(env::args()).unwrap_or_else(|e| {
    eprintln!("Problem parsing Arguments: {}", e);
    process::exit(1);
  });

  if let Err(e) = minigrep::run(&config) {
    eprintln!("Application Error {}", e);
  } 
}

/* NOTES
 
Result's unwrap_or_else()
- if Ok(s) return s
- if Err(e) do closure function |e| { f(e); }

if let err(e) = f() { g(e); }
- run function `f`, if err(e) received from f, run g(e)
 
collect()
- iterate over values and pass it as a collection (like vec or hashmap) 

eprintln!("{}", e);
- prints to the standard error stream
- `println!` capable of printing to standard output 
  not standard error to we need to use this
- stderr, stdout

 */
