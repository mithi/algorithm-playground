### Debugging
- Test driven development (TDD)
- RSpec automated testing

### Exception handling
- `ArgumentError`, `NameError`, `NoMethodError`, `IndexError`, `TypeError`
```ruby
def format_name(first, last)
  if !(first.instance_of?(String) && last.instance_of?(String))
    raise "arguments must be strings"
  end

  first.capitalize + " " + last.capitalize
end

first_name = 42
last_name = true
begin
  puts format_name(first_name, last_name)
rescue
  # do stuff to rescue the "arguments must be strings" exception...
  puts "there was an exception :("
end
```

### Pry
```ruby
> ls String
> show-doc String#end_with?
```
```ruby
$ pry
> load "code.rb"
=> true
> divisible(21, 8)
=> false
> show-source divisible

From: code.rb @ line 1:
Owner: Object
Visibility: private
Number of lines: 3

def divisible(n, d)
  n % d == 0 ? true : false
end
>
```

### ByeBug
```
require "byebug"
debugger
l <start line>-<end line>
step or s
next or n
break <line num> or b <line num>
continue or c
display <variable>
```

