# Smart Pointers 
- `Box<T>` 
- `Rc<T>`
- `RefCell<T>` 
- Source: The Rust Programming Language - Nicholas Matsakis and Aaron Turon

# Recap


# Pointer vs Smart Pointer
- pointer
  - a general concept for a variable that contains an address in memory
  - a reference - most common kind of pointer, `y = &x`, no overhead 
- smart pointer 
  - pointer with additional metadata and capabilities
  - examples: `String`, `Vec<T>` 
  - usually implemented using `structs` with `Deref` + `Drop` traits
  - Commonly used smart Pointers: - `Box<T>`, `Rc<T>`, `RefCell<T>` 


# `Box<T>` 
- Data stored in the heap (not stack), most data are stack-allocated by default

## Situations where `Box` maybe used: 
- When you have a type with size that can't be known at compile time and you want to use a value of that type in a context that needs to know an exact size. 
- When you have a large amount of data and you want to transfer ownership. but ensure that the data won't be copied when you do so
- When you want to own a value and only care that it is a type that implements a particular trait rather than knowing the contrete type 

## Example Situation: `Box` enables recursive types
- At compile time Rust needs to know how much space a type takes up. A recursive type is a type where a value can have as a part of itself another value of the same type.
- Instead of a `List` containing a number and another `List` which won't compile, make the `List` contain a number an a pointer to another `List`

```rust 
// Example of recursive type that wont compile
// A `List` is either a `Cons` or `Nil`
// `Cons` has a number and a `List`
// Will not compile 

enum List {
  Cons(i32, List),
  Nil,
} 

use List::{Cons, Nil};

fn main() {
    let a = Cons(1, Cons(2, Cons(3, Nil)));
}

// recursive type has infinite size
// recursive without indirection
```
- Write it like this instead, this one will compile 
```rust 

use std::fmt;
use List::{Cons, Nil};

enum List {
  Cons(i32, Box<List>), 
  Nil,
}

impl fmt::Display for List {
  fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
    match self {
      Nil => write!(f, "NIL"),
      Cons(i, _) => write!(f, "{}", i),
    }
  }
}

fn main() {
    let a = Cons(1,
      Box::new(Cons(2,
        Box::new(Cons(3,
          Box::new(Nil))))));
    
    let b = Nil;
    let c = Cons(4, Box::new(Nil));
    
    println!("{}", a); // 1
    println!("{}", b); // NIL
    println!("{}", c); // 4
}
```

## `Deref` and Deref Coercion
- We can treat smart pointers like regular references with `Deref` trait
- Sample implementation `MyBox`
```rust 

use std::ops::Deref;

struct MyBox<T>(T);

impl<T> MyBox<T> {
  fn new(x: T) -> MyBox<T> {
    MyBox(x)
  }
}

impl<T> Deref for MyBox<T> {
  type Target = T;

  fn deref(&self) -> &T {
    &self.0
  }
}

fn hello(name: &str) {
    println!("Hello, {}!", name);
}

fn main() {

  let x = 5;
  let y = MyBox::new(x);

  assert_eq!(5, x);
  assert_eq!(5, *(y.deref()));
  assert_eq!(5, *y);
  // *y implicitly does *(y.deref())

  let m = MyBox::new(String::from("Rust"));
  hello(&m); // Hello, Rust
  hello(&(*m)[..]); // Hello, Rust
  // Rust performs deref coercion on &m
  // so we don't need to write &(*m)[..]
  // Rust calls `deref`
  // &MyBox<String> to &String b
  // Rust calls `deref` again
  // &String to &str
  // which matches `hello` function definition
}
```
> Deref coercion converts a reference to a type that implements `Deref` into a reference to a type that `Deref` can convert the original type into.
- A convenience that Rust performs on arguments to functions and methods
- Happens automatically, a sequence of calls to `deref` method converts the type we provided into the type the parameter needs
- So we don't need to add many explicit references `&` and dereferences `*`
- No runtime penalty 
- Rust DOES NOT COERCE immutable references to mutable references! bu you can coerce mutable reference to an immutable one
- From `&T` to `&U` when `T: Deref<Target=U>`
- From &mut `T` to `&mut U` when `T: DerefMut<Target=U>`
- From `&mut T` to `&U` when `T: Deref<Target=U>`

## `Drop`
- Use the `Drop` trait to customize what happens when value goes out of scope. 
- Often used to release resources or network connections 
- Example: `Box<T>` customizes `Drop` to deallocate the space on the heap that the box points to
- `Drop` will be called when a value goes out of scope so that we don't have to be careful to place cleanup code and won't leak resources
- Variables are dropped in the reverse order of the order in which they were created.
- We can't explicitly call the destructor like  `object.drop()`  because rust wil call it again at the end of `main`, this is a double free error, because use would try to cleanup the same value twice. 
- Use `std::mem::drop` instead. 
```rust 

use std::mem::drop;

struct CustomSmartPointer {
  data: String,
}

impl Drop for CustomSmartPointer {
  fn drop(&mut self) {
    println!("Dropping CustomSmartPointer with data `{}`!", self.data);
  }
}

fn main() {
  let c = CustomSmartPointer { data: String::from("-c!") };
  let d = CustomSmartPointer { data: String::from("-d!") };
  let e = CustomSmartPointer { data: String::from("-e!") };
  println!("CustomSmartPointers created.");    
  println!("c: {}, d: {}, d: {},", c.data, d.data, e.data);
  drop(d);
  println!("CustomSmartPointer dropped before the end of main.");
}

```
- Don't worry about accidentally cleaning up values still in use because that would cause a compiler error.
```
CustomSmartPointers created.
c: -c!, d: -d!, d: -e!,
Dropping CustomSmartPointer with data `-d!`!
CustomSmartPointer dropped before the end of main.
Dropping CustomSmartPointer with data `-e!`!
Dropping CustomSmartPointer with data `-c!`!
```

# `Rc<T>` the Reference Counted Smart Pointer 
- only for use in single-threaded scenarios, `aRc<T>` on multi-threaded scenarios
- keeps track of the number of references to a value to know whether or not a value is still in use.

## EXAMPLES
> Imagine `Rc<T>` as a TV in a family room. When one person enters to watch TV, they turn it on. Others can come into the room and watch the TV. When the last person leaves the room, they turn off the TV because it’s no longer being used. If someone turns off the TV while others are still watching it, there would be uproar from the remaining TV watchers!
>  In graph data structures, multiple edges might point to the same node, and that node is conceptually owned by all of the edges that point to it. A node shouldn’t be cleaned up unless it doesn’t have any edges pointing to it.

## SAMPLE CODE
```rust
enum List {
  Cons(i32, Rc<List>),
  Nil,
}

use List::{Cons, Nil};
use std::rc::Rc;

fn main() {
  let a = Rc::new(Cons(5, Rc::new(Cons(10, Rc::new(Nil)))));
  println!("count after creating a = {}", Rc::strong_count(&a));
  
  let b = Cons(3, Rc::clone(&a));
  println!("count after creating b = {}", Rc::strong_count(&a));
  
  {
    let c = Cons(4, Rc::clone(&a));
    println!("count after creating c = {}", Rc::strong_count(&a));
  }
  
  println!("count after c goes out of scope = {}", Rc::strong_count(&a));
}
```

- This code prints the following:
```
count after creating a = 1
count after creating b = 2
count after creating c = 3
count after c goes out of scope = 2
```
- Diagram
```

b -> [3][]------\
c -> [4][]----| |
              v v
a ----------->[5][]--->[10][]---> Nil

```
## `Rc::clone(&a)` vs `a.clone()`
- `Rc::clone(&a)` doesn't make a deep copy, only 
- `a.clone()` makes a deep copy like most implementations of `clone` does on other data types
- `Rc::clone` only increases reference count


# `RefCell<T>`
- Only used for single threaded scenarios
- Useful when you're sure your code follows the borrowing rules, but the compiler is unable to understand or guarantee that.

## Recall borrowing rules
1. At any given time you can have either but not both:
  - One mutable reference
  - Any number of immutable references
2. References must always be valid

## Recap 

- `Rc<T>` enables multiple owners of the same data; 
- `Box<T>` and `RefCell<T>` have single owners.
- `Box<T>` allows immutable or mutable borrows checked at compile time; 
- `Rc<T>` only allows immutable borrows checked at compile time; 
- `RefCell<T>` allows immutable or mutable borrows checked at runtime.
- Because `RefCell<T>` allows mutable borrows checked at runtime, we can mutate the value inside the 
  `RefCell<T>` even when the `RefCell<T>` is immutable.

# TO BE CONTINUED
- `RefCell<T>` and the Interior Mutability Pattern
- Reference Cycles Can Leak Memory


