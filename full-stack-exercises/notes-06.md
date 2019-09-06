
```ruby
# spaceship operator
7 <=> 2     # => 1
7 <=> 7     # => 0
2 <=> 7     # => -1
```
- nil and false are the only falsey values
- everything else is truthy
```ruby
a || b
```
- when a is truthy, return a
- when a is falsey, return b

#### Default Arguments
```ruby
def greet(person = nil)
    #person = person || "you"
    person ||= "you"
    p "Hey " + person
end

greet("Brian")  # => "Hey Brian"
greet           # => "Hey you"
```

#### Default Procs
```ruby
def call_that_proc(val, &prc)
    prc ||= Proc.new { |data| data.upcase + "!!" }
    prc.call(val)
end

p call_that_proc("hey")
# => "HEY!!"
p call_that_proc("programmers") { |data| data * 3 }
# => "programmersprogrammersprogrammers"
p call_that_proc("code") { |data| "--" + data.capitalize + "--"}
# => "--Code--"
```

#### Lazy Initialization
- only create the `@menu` if someone asks for it
```ruby
class Restaurant
    attr_accessor :name, :chefs, :menu

    def initialize(name, chefs)
        @name = name
        @chefs = chefs
    end

    def menu
        @menu ||= ["sammies", "big ol' cookies", "bean blankies", "chicky catch", "super water"]
    end
end

five_star_restaurant = Restaurant.new("Appetizer Academy", ["Marta", "Jon", "Soon-Mi"])

p five_star_restaurant
#<Restaurant:0x00007f90b3922368
# @name="Appetizer Academy",
# @chefs=["Marta", "Jon", "Soon-Mi"]
#>

p five_star_restaurant.menu
#["sammies", "big ol' cookies", "bean blankies", "chicky catch", "super water"]

p five_star_restaurant
#<Restaurant:0x00007f90b3922368
# @name="Appetizer Academy",
# @chefs=["Marta", "Jon", "Soon-Mi"],
# @menu=["sammies", "big ol' cookies", "bean blankies", "chicky catch", "super water"]
#>
```
