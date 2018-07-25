use std::collections::HashMap; 

fn main() {

//-----------------------
// Inserting values
//-----------------------
  let mut scores = HashMap::new();
  scores.insert(String::from("Blue"), 10);
  scores.insert(String::from("Yellow"), 50);
  println!("0A. {:?}", scores); //{"Yellow": 50, "Blue": 10}
  // Given a hashmap, all keys must have same type,
  // all values must also have same type
  
  let field_name = String::from("Favorite color");
  let field_value = String::from("Blue");
  let mut map0 = HashMap::new();
  // You can insert references to HashMap
  // just be sure that what you insert has the same 
  // lifetime as the hashmap or longer
  map0.insert(&field_name, &field_value);
  //Note: values not consumed by println
  println!("0B. {:?}, {:?}", field_name, field_value); // "Favorite color", "Blue" 
  println!("0C. {:?}, {:?}", field_name, field_value); // "Favorite color", "Blue" 


  let name = String::from("Favorite color");
  let value = String::from("Blue");
  let mut map1 = HashMap::new();
  map1.insert(name, value);
  // name and value are invalid at this point
  {
    let (k, v) = ("myKey".to_string(), "myValue".to_string());
    // ownership has been passed
    map1.insert(k, v);
  }
  println!("1A. {:?}", map1); // {"Favorite color": "Blue", "myKey": "myValue"}

  
  let my_keys = vec![String::from("Blue"), String::from("Yellow")];
  let my_values = vec![10, 50];
  let my_map: HashMap<_, _> = my_keys.iter().zip(my_values.iter()).collect();
  println!("2A. {:?}", my_map); // {"Yellow": 50, "Blue": 10}
  
//-----------------------
// Accessing values
//-----------------------

  // IMPORTANT: hashmap returns Option<&V>, - nonmutable reference
  // IMPORTANT: hashmap.get() expects reference not ownership
  println!("2B. {:?}", scores.get(&"Red".to_string())); // None
  println!("3. {:?}", scores.get(&"Blue".to_string())); // Some(10)
  // passing "Blue".to_string() results error "expected reference found struct..."
  let team = String::from("Blue");
  println!("4. {:?}", scores.get(&team)); //Some(10)

  /*
  println!("{:?}", scores.get(team));
  Will not work, expects reference
  */

  // prints each pair in an arbitrary order
  for (key, value) in &scores {
    println!("5. {}: {}", key, value); 
  }
  // "Blue", 10
  // "Yellow", 50
  
  // or use chaining
  scores.iter().for_each( |(k, v)| println!("6. {:?}, {:?}", k, v));
  // "Blue", 10
  // "Yellow", 50

//-----------------------
// Updating a hashmap
//-----------------------

  // Overwriting a value
  scores.insert(String::from("Blue"), 15);
  println!("7. {:?}", scores); // {"Yellow": 50, "Blue": 10}
  scores.insert(String::from("Blue"), 25);
  println!("8. {:?}", scores); // {"Yellow": 50, "Blue": 25}

  // Only Inserting a Value If the Key Has No Value
  scores.entry(String::from("Yellow")).or_insert(100);
  scores.entry(String::from("Blue")).or_insert(10);
  println!("9. {:?}", scores); // {"Yellow": 50, "Blue": 25}

  // Updating a Value Based on the Old Value
  let text = "hello world wonderful world";
  let mut map = HashMap::new();

    for word in text.split_whitespace() {
      let count = map.entry(word).or_insert(0);
      *count += 1;
  }

  println!("10. {:?}", map); // {"world": 2, "hello": 1, "wonderful": 1}
  // or_insert method actually returns a mutable reference (&mut V)
}