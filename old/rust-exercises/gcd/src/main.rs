// `Write` and `FromStr` are `traits`
// `use` declaration brings them to scope
// so we can use their methods 
use std::io::Write;
use std::str::FromStr;

// Function doesnt return anything, no need for `->` 
fn main() {

  // `!` indicates macro invocation not a function call
  println!("..........................");
  println!("HELLO WORLD! HELLO GCD!");
  println!("..........................");

  // like a C++ std::vector or Python list
  // We can infer based on what we push onto it
  //  Vec<u64>::new()
  let mut numbers = Vec::new();
  
  // `args()` function is an `iterator`
  // `iterator` - value that produces each argument on demand
  // and indicates when we are done
  // used on almost anything we have to loop over
  // the first value returned by `args()` is
  // the name of the program being run.
  // `skip(1)` produces new iterator that omits first value
  for arg in std::env::args().skip(1) {

    // `u64::from_str()` attempts to parse commandline `arg` as a u64
    // `from_str()` returns a `Result` type value
    // `Result` is either Ok(v) or Err(e)
    // Ok(v), parse succeeded, v: value produced
    // Err(e), parse failed, e: value explaining why
    // Rust does not have exceptions, all errorshandled 
    // using `Result` or `panic`
    // `&arg` is pointer to `arg` ???
    // in case the result is Err(e) is `expect()`
    // to tell user why program crashed
  	let x = u64::from_str(&arg)
  	           .expect("error parsing argument");

    // push onto end of vector
  	numbers.push(x);
  }

  // `numbers` should have atleast one element
  // else exit the program
  // use `writeln` to write inform user why program exit
  // `.unwrap()` checks if error message itself did not itself fail 
  if numbers.len() == 0 {

    println!("--> Sample Usage: ");
    println!("     $ cargo run 42 46 4 8");
    println!("     $ The greatest common divisor of [42, 46, 4, 8] is 2");
    writeln!(std::io::stderr(), 
  		     "Error! Usage! Try: $ cargo run 42 46 4 8").unwrap();
    
  	std::process::exit(1);
  }

  // put first value in `d`
  let mut d = numbers[0];

  // `&` indicates the ownership of the vector should remain in `numbers`
  // we're borrowing a references to elements of the vector
  // we give it back when we're done
  // reference stored in `m` 
  // use `*` to get value stored in reference `m` 
  // `*m` dereferences `m` 
  for m in &numbers[1..] {
    d = gcd(d, *m);
  }

  // `{:?}` print depends on `display trait`
  println!("The greatest common divisor of {:?} is {}", 
  	        numbers, d);
}

// ............................................
// GCD + TEST
// ............................................

// `#[test]` is an `attribute`
// open-ended system for marking functions/ other declarations
// with extra information
// used to control compiler warnings, code style checks
// include code conditionally etc etc  
#[test]
fn test_gcd() {

  let x = 2 * 3 * 5 * 11 * 17;
  let y = 3 * 7 * 11 * 13 * 19;
  let z = 3 * 11;
  
  assert_eq!(gcd(x, y), z);
  assert_eq!(gcd(14, 15), 1);
}


// variables immutable unless explicitly declared mutable
// must write out types of function parameters
// and return type -> u64 
fn gcd(mut n: u64, mut m: u64) -> u64 {

  assert!(n != 0 && m != 0);

  while m != 0 {

    if m < n {
      // can infer variable types within function bodies 
      // let t: u64 = m  
      let t = m;
      m = n;
      n = t;
    }

    m = m % n; 
  }

  // if function body ends with an expression 
  // that's not followed by a semicolon
  // that's the function's return value
  n 
}



