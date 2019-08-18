### No Scope
- Blocks, conditionals or while loops also don't have their own scope. they are really a part of the containing method's scope.
```ruby
def say_bye
    message = "bye"

    3.times do
        p message
    end
end

say_bye
```
```ruby
if true
    drink = "cortado"
end

p drink
```
### Local scope
```ruby
message = "hi"

def say_hello
    p message   # NameError: undefined local variable
end
```
```ruby
def say_hello
    message = "hello"
end

say_hello
p message   # NameError: undefined local variable
```
### Global variables and constants
```ruby
$message = "hello globe"

def say_hello
    p $message
end

say_hello # => "hello globe"
```
```ruby
def say_hello
    $message = "hello globe"
end

say_hello
p $message # => "hello globe"
```
```
FOOD = "pho"
p FOOD # => "pho"

FOOD = "ramen"  #warning: already initialized constant FOOD
                #warning: previous definition of FOOD was here
```
> while you cannot reassign a constant, you can still mutate that constant name without warning:
```ruby
FOOD = "pho"
FOOD[0] = "P"
p FOOD # => "Pho
```
```
FOOD = "pho"
$drink = "ice coffee"

def my_favorite
    p FOOD
    p $drink
end

my_favorite
```
