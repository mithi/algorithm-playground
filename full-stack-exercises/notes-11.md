### Equality
- Value equality `==` vs hash equality `.eql?()`

### Value Equality `#==`
`#==` is inherited from the Object class. By default, it will return true if and only if the two objects are literally the same object (pointer equality). This default behavior is not particularly helpful, so you should override it

### Hash Equality `#eql?`
`a.eql? b` is equivalent to `a.hash == b.hash`
```ruby
   3.0 == 3 #=> true
   3.0.eql? 3 #=> false
```
- to provide a meaningful `#eql?` method for your classes, you will need to override the `#hash` method.
`#eql?` is used by `Hash` to check if an object is a key in a hash

```
some_array = [1]
some_hash = { some_array => 'secrets' }
some_array << 2
some_hash[some_array] #=> ???
```

### Identity Equality `#equal?`
- `#equal?` does simple identity comparison (pointer comparison). i.e. `a.equal? b` if and only if `a` is the same object as `b`. This is identical to the default behavior of` #==` in the `Object` class
- SHOULD NEVER BE OVERRIDDEN
```ruby
a = Dog.new
b = Dog.new
a = c

a.equal? b #=> false
a.equal? c #=> true
```

### Case Equality `#===`
```ruby
[pry]--> String == "hello"
=> false
[pry]--> String === "hello"
=> true
[pry]--> "hello" === String
=> false
[pry]--> "hello" == String
=> false
```
`#===` has the same behavior as `#==` for most classes (and by default for classes that you write). This is the method that case uses to determine which block to execute.
```ruby
case a
when b
   # ...
when c
   # ...
else
   # ...
end
```
is equivalent to
```ruby
if b === a # triple equals!
   # ...
elsif c === a
   # ...
else
   # ...
end
```
- stackoverflow.com/a/1735777 how to refactor with `Regexp#===`

```ruby
case number
when Integer
   # ...
when Float
   # ...
end
```
The takeaway is that if you have created a class and you want to use it as a key in a hash, you should define #hash and #eql?.


### Links
- https://ruby-doc.org/core-2.1.2/Object.html
- https://stackoverflow.com/questions/7156955/whats-the-difference-between-equal-eql-and/7157051#7157051
