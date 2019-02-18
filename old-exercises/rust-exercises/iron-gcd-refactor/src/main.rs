#[macro_use] extern crate mime; 
extern crate iron;
extern crate router;
extern crate urlencoded;

use iron::prelude::*;
use iron::status;
use router::Router;
use std::str::FromStr;
use urlencoded::UrlEncodedBody;


fn main() {

  let mut router = Router::new();

  // Configure callback functions for HTTP request-response protocol
  router.get("/", get_form, "root");
  router.get("/hello", say_hello, "hello");
  router.post("/gcd", post_gcd, "gcd");

  println!("Serving on http://localhost:3000...");
  Iron::new(router).http("localhost:3000").unwrap();
}


// Convert a vector of Strings to a vector of u64 numbers
fn strings_to_numbers(string_numbers: &[String]) -> Result<Vec<u64>, String> {
  let mut numbers = Vec::new();
  
  for string_number in string_numbers {    
    match u64::from_str(&string_number) {
      Err(_) => return Err(string_number.clone().to_string()),
      Ok(n) => numbers.push(n),
    }
  }

  Ok(numbers)
}


// Does this vector contain a zero? 
fn has_zero(numbers: &[u64]) -> bool {
  for m in numbers.iter() {
    if *m == 0u64 { return true };
  }
  false
}


// Euclid's Algorithm
fn gcd(mut n: u64, mut m: u64) -> u64 {
  assert!(n != 0 && m != 0);

  while m != 0 {
    if m < n {
      let t = m;
      m = n;
      n = t;
    }

    m = m % n
  }
  n 
}


// Greatest common denominator given a vector of numbers
fn gcd_answer(numbers: &[u64]) -> u64 {

  let mut d = numbers[0];

  for m in &numbers[1..] {    
    d = gcd(d, *m)
  }
  d
}


// Publish gcd submission form at server's `root`
fn get_form(_request: &mut Request) -> IronResult<Response> {
  let mut response = Response::new();
  
  response.set_mut(status::Ok);
  response.set_mut(mime!(Text/Html; Charset=Utf8));

  response.set_mut(r#"
    <title>GCD Calculator</title>
    <form action="/gcd" method="post">
      <input type="text" name="n" />
      <input type="text" name="n" /> 
      <input type="text" name="n" /> 
      <input type="text" name="n" /> 
      <button type="submit"> Compute GCD </button>
     </form>
  "#);
  
  Ok(response)
}


// Return when client requests `/hello`
fn say_hello(_request: &mut Request) -> IronResult<Response> {
  let mut response = Response::new();
  response.set_mut(status::Ok);
  response.set_mut(mime!(Text/Html; Charset=Utf8));
  response.set_mut("Hello World!".to_string());
  Ok(response)
}


// Parse client's http request to get gcd given set of numbers
// Return http response after computing gcd if successful
// else report error to client 
fn post_gcd(request: &mut Request) -> IronResult<Response> {

  // Convert `Request` to a table mapping the query parameter to a vector of values  
  let form_data = match request.get_ref::<UrlEncodedBody>() {
    Err(e) => return bad_response(format!("Error parsing form data: {:?}", e)),
    Ok(map) => map,
  };
  
  // Get value of parameter `n` which is a `String` vector 
  let string_numbers = match form_data.get("n") {
    None => return bad_response("form data has no 'n' parameter".to_string()),
    Some(nums) => nums,
  };

  // Convert a vector of Strings to a vector of u64 numbers
  let numbers = match strings_to_numbers(&string_numbers) {
    Err(s) => return bad_response(format!("Value for 'n' parameter not a number {:?}", s)),
    Ok(nums) => nums,
  };
  
  // Check if one of the elements is zero 
  if has_zero(&numbers) {
    return bad_response("At least one of the values is 0".to_string());
  }

  successful_gcd_response(&numbers, gcd_answer(&numbers))
}


// http response given vector of numbers and its gcd
fn successful_gcd_response(numbers: &[u64], d: u64) -> IronResult<Response> {

  let mut response = Response::new();
  response.set_mut(status::Ok);
  response.set_mut(mime!(Text/Html; Charset=Utf8));
  response.set_mut(
    format!("The greatest common divisor of the numbers {:?} is <b>{}</b>\n",
            numbers, d));

  Ok(response)
}


// http response given error (to client asking for gcd)  
fn bad_response(message: String) -> IronResult<Response> {
  let mut response = Response::new();
  response.set_mut(status::BadRequest);
  response.set_mut(message);
  Ok(response)
}
