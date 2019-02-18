# GCD
# Test
```
$ cargo test

   Compiling gcd v0.1.0 (file://..../gcd/)
    Finished dev [unoptimized + debuginfo] target(s) in 0.68 secs
     Running `..../gcd/target/debug/gcd`

running 1 test
test test_gcd ... ok

test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

# Run 
```
$ cargo run

   Compiling gcd v0.1.0 (file://..../gcd/)
    Finished dev [unoptimized + debuginfo] target(s) in 0.68 secs
     Running `..../gcd/target/debug/gcd`

..........................
HELLO WORLD! HELLO GCD!
..........................
--> Sample Usage: 
     $ cargo run 42 46 4 8
     $ The greatest common divisor of [42, 46, 4, 8] is 2
Error! Usage! Try: $ cargo run 42 46 4 8
```

# Run with arguments 
```
$ cargo run 42 46 4 8 14

   Compiling gcd v0.1.0 (file://..../gcd/)
    Finished dev [unoptimized + debuginfo] target(s) in 0.68 secs
     Running `..../gcd/target/debug/gcd`

..........................
HELLO WORLD! HELLO GCD!
..........................
The greatest common divisor of [42, 46, 4, 8, 14] is 2
```

# Clean
```
$ cargo clean
```
