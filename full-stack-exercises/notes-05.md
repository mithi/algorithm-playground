### Class Basics
- Monkey-patching lets you add new methods in an existing class
- an `@instance_variable` will be a distinct variable in each instance of a class; changing the variable will only effect that one instance
- a `@@class_variable` will be shared among all instances of a class; changing the variable will effect all instances because all instances of the class
- a `CLASS_CONSTANT` will be shared among all instances of a class, but cannot be changed
- `Class#method_name `- an instance method
- `Class::method_name`-is a class method
```ruby
class Hello
  def self.this_class_method
    puts "This is a class method"
  end
end
```
- Separation of Concerns. One file should focus on implementing one class

```
project_root
  ├── pet_hotel.rb
  ├── cat.rb
  └── other_animals
      └── dog.rb
```

- requiring for `pet_hotel.rb`
```ruby
require_relative "./cat.rb"
require_relative "./other_animals/dog.rb"
```
- Use the plain `require` where gems are involved. ruby already knows where to find `byebug` through the `$LOADPATH`

```ruby
my_string = "yes\n"
p my_string       # "yes\n"
p my_string.chomp # "yes"
```

### Abstraction + Encapsulation
- Abstraction - exposing essential features of an object while hiding inner details that are not necessary to using the feature
- encapsulation closely relates methods and data attributes together with the hope of preventing misuse. give users access to the things that are safe for them to use, others kept private `getter` and `setter`

### Attribute methods
```ruby
class Dog
  # attr_accessor will define #name, #name=, #age, #age= methods for us
  attr_accessor :name, :age

  def initialize(name, age, favorite_food)
    @name = name
    @age = age
    @favorite_food = favorite_food
  end
end

dog = Dog.new("Fido", 3, "pizza")

# Let's use the setter and getter for name!
dog.name = "Spot"
p dog.name          # "Spot"
```
- `attr_reader` abd `attr_writer`

### Syntactic Sugar
```
p person_1.==(person_2)
p person_1 == person_2
```
```
grocery_checkout.[](1)
grocery_checkout[1]
```
```
grocery_checkout.[]=(0, "Grace")
grocery_checkout[0] = "Grace"
```
