# An I/O Project: Building a Command Line Program
- [Source: The Rust Programming Language: 2nd Edition](https://doc.rust-lang.org/book/second-edition/ch12-00-an-io-project.html#an-io-project-building-a-command-line-program)

# test 
```sh
$ cargo test
--snip--

running 2 tests
test test::case_sensitive ... ok
test test::case_insensitive ... ok

test result: ok. 2 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

     Running ../rust-playground/minigrep/target/debug/deps/minigrep-a6f02322bb32752c

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out

   Doc-tests minigrep

running 0 tests

test result: ok. 0 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out
```

# Sample 1

```sh
$ CASE_INSENSITIVE=0 cargo run to ./data-input/poem.txt
--snip--

...Finished search for `to`, in file `../data-input/poem.txt` with case sensitivity set to `false` 

OUTPUT: 

Are you nobody, too?
How dreary to be somebody!
To tell your name the livelong day
To an admiring bog!

INPUT: 

I’m nobody! Who are you?
Are you nobody, too?
Then there’s a pair of us — don’t tell!
They’d banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!
```

# Sample 2

```sh
$ cargo run to ./data-input/poem.txt
--snip--


...Finished search for `to`, in file `../data-input/poem.txt` with case sensitivity set to `true` 

OUTPUT: 

Are you nobody, too?
How dreary to be somebody!

INPUT: 

I’m nobody! Who are you?
Are you nobody, too?
Then there’s a pair of us — don’t tell!
They’d banish us, you know.

How dreary to be somebody!
How public, like a frog
To tell your name the livelong day
To an admiring bog!

```

# Additional Samples
```sh
$ cargo run to ./data-input/poem.txt > ./data-output/poem-output-true.txt
$ CASE_INSENSITIVE=1 cargo run to ./data-input/poem.txt > ./data-output/poem-output-false.txt
```
