use std::error::Error;
use std::fs::File;
use std::io::prelude::*;
use std::env; 

pub struct Config {
  query: String, 
  filename: String,
  case_sensitive: bool,
}

impl Config {
  pub fn new(mut args: std::env::Args) -> Result<Config, &'static str> {

    args.next();

    let query = match args.next() {
      Some(arg) => arg,
      None => return Err("Didn't get a query string"),
    };

    let filename = match args.next() {
      Some(arg) => arg,
      None => return Err("Didn't get a file name"),
    };

    let case_sensitive = env::var("CASE_INSENSITIVE").is_err();

    Ok(Config { query, filename, case_sensitive })
  }
}


fn output_results(config: &Config, contents: &str, results_vec: &[&str]) {

  println!("\n\n...Finished search for `{}`, in file `{}` with case sensitivity set to `{}` \n",
    &config.query, &config.filename, &config.case_sensitive);

  println!("OUTPUT: \n");
  results_vec.iter().for_each(|line| println!("{}", line));
  
  println!("\nINPUT: \n\n{}\n", &contents);    
}


fn sensitive_search<'a>(query: &str, contents: &'a str) -> Vec<&'a str>  {
  contents.lines().filter(|line| line.contains(query)).collect()
}


fn insensitive_search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
  let new_query = &query.to_lowercase();
  contents.lines().filter(|line| line.to_lowercase().contains(new_query)).collect()  
}


fn search<'a>(query: &str, case_sensitive: bool, contents: &'a str) ->  Vec<&'a str> {
  // return a vec of references to lines in `contents` containing string `query`
  
  if case_sensitive { 
    sensitive_search(&query, &contents)
  } else {
    insensitive_search(&query, &contents)
  }
}


pub fn run(config: &Config) -> Result<(), Box<Error>>{

  // read and store file contents in memory
  let mut file = File::open(&config.filename)?;
  let mut contents = String::new();
  file.read_to_string(&mut contents)?;
  
  // search for query word given file contents, then display to user
  let results_vec = search(&config.query, config.case_sensitive, &contents);
  output_results(&config, &contents, &results_vec);
  Ok(())
}

#[cfg(test)]
mod test {
  use super::*;

  #[test]
  fn case_sensitive() {
    let contents = "\
      Rust:\n\
      safe, fast, productive.\n\
      Pick Three.\n\
      Duct tape.";

    assert_eq!(vec!["safe, fast, productive."], search("duct", true, contents));
  }

  #[test]
  fn case_insensitive() {
    let contents = "\
      Rust:\n\
      safe, fast, productive.\n\
      Pick Three.\n\
      Trust me.";

    assert_eq!(vec!["Rust:", "Trust me."], search("rUsT", false, contents));
  }
}

/* NOTES
 
super::*;
- Way to navigate from your current module to its parent 

#[cfg(test)]

&'static str
- The error string lives until the program exits  

? 
If called function g (in function f) returns error, f returns error (exit f early) 

'a
fn example_function<'a>(x: &T, y: &'a T) -> Vec<&'a T> {} 
- 'a specifies a lifetime 
- the lifetime parameters specify which argument lifetime is connected 
  to the lifetime of the return value
- this means in this example  that the return vector
- if you have a return type which contains a reference `&` 
and two arguments with with references, then logically it means
that the return variable must have a reference to at least one of the arguments
- these arguments may or may not have the same lifetime 

env::var("environment name").is_err()
- returns a Result, with `Ok` containing value of environment variable
- `is_err()` returns `false` in case of error 
 */