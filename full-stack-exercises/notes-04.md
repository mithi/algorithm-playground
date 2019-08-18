# Blocks

- `return` keyword pertains to methods, not blocks

```ruby
["a", "b", "c"].map { |str| str.upcase }  #=> ["A", "B", "C"]
["a", "b", "c"].map(&:upcase) #=> ["A", "B", "C"]

[1, 2, 5].select { |num| num.odd? }       #=> [1, 5]
[1, 2, 5].select(&:odd?)      #=> [1, 5]

array.map { |block_param| block_param.method }
array.map(&:method)
```

# Procs

- an object that contains a block.
- allow us to save blocks to variables

```ruby
doubler = Proc.new { |num| num * 2 }
p doubler # #<Proc:0x00007f9a8b36b0c8>
p doubler.call(5) # => 10
p doubler.call(7) # => 14
```
- Because of the `&prc` parameter we must always pass a `block` into `add_and_proc`, we can no longer pass in a `proc` because a conversion from `block` to `proc` must take place.

```ruby
def add_and_proc(num_1, num_2, prc)
  sum = num_1 + num_2
  p prc.call(sum)
end

doubler = Proc.new { |num| num * 2 }
add_and_proc(1, 4, doubler)   # => 10
```

- `&` can be used to convert a `block` into a `proc`. But it can also be used for the opposite, that is, convert a `proc` into a `block`.

```ruby
def add_and_proc(num_1, num_2, &prc)
  sum = num_1 + num_2
  p prc.call(sum)
end

add_and_proc(1, 4) { |num| num * 2 }  # => 10

doubler = Proc.new { |num| num * 2 }
add_and_proc(1, 4, &doubler)   # => 10

add_and_proc(1, 4, doubler)
# ArgumentError: wrong number of arguments (given 3, expected 2)
```
```ruby
[1,2,3].map { |num| num * 2 } # => [2, 4, 6]
doubler = Proc.new { |num| num * 2 }
[1,2,3].map(&doubler) # => [2, 4, 6]
```
