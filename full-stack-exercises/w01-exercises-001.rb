# Arrays
# Enumerables
# Hashes
# Map and Select
# Option and Hashes

# The "Ruby Way"
# Symbols
# Default arguments
# Splat operators
# Inject aka reduce

# Scope
# Methods and Local Scope
# lexical scope.
# how variable names resolve if we put them in structures
# like methods, conditionals, or blocks

# Less preferred
# def get_avg(num_1, num_2)
#    return (num_1 + num_2) / 2
# end

# Preferred by a Rubyist
def get_avg(num_1, num_2)
    (num_1 + num_2) / 2
end

def say_hi
    puts "hi"
end

# Less preferred
# say_hi()

# Preferred by a Rubyist
say_hi

raining = true
# Less preferred
# if raining
#    puts "don't forget an umbrella!"
# end

# Preferred by a Rubyist
puts "don't forget an umbrella!" if raining

num = 6

# Less preferred
# p num % 2 == 0

# Preferred by a Rubyist
p num.even?

people = ["Joey", "Bex", "Andrew"]

# Less preferred
# p people[people.length - 1]

# Preferred by a Rubyist
p people[-1]
p people.last

# Less preferred
# def repeat_hi(num)
#     i = 0
#     while i < num
#         puts "hi"
#         i += 1
#     end
# end

# Preferred by a Rubyist
def repeat_hi(num)
    num.times { puts "hi" }
end

# Less preferred
# def all_numbers_even?(nums)
#     nums.each do |num|
#         return false if num % 2 != 0
#     end
#     true
# end

# Preferred by a Rubyist
def all_numbers_even?(nums)
    nums.all? { |num| num.even? }
end


# all?
# Return true when all elements result in true when passed into the block.
p [2, 4, 6].all? { |el| el.even? }  # => true
p [2, 3, 6].all? { |el| el.even? }  # => false

# any?
# Return true when all at least one element results in true when passed into the block.
p [3, 4, 7].any? { |el| el.even? }  # => true
p [3, 5, 7].any? { |el| el.even? }  # => false

# none?
# Return true when no elements of result in true when passed into the block
p [1, 3, 5].none? { |el| el.even? } # => true
p [1, 4, 5].none? { |el| el.even? } # => false

# one?
# Return true when exactly one element results in true when passed into the block.
p [1, 4, 5].one? { |el| el.even? }  # => true
p [1, 4, 6].one? { |el| el.even? }  # => false
p [1, 3, 5].one? { |el| el.even? }  # => false


# count
# Return a number representing the count of elements that
# result in true when passed into the block.

p [1, 2, 3, 4, 5, 6].count { |el| el.even? }    # => 3
p [1, 3, 5].count { |el| el.even? }             # => 0

#Return the total sum of all elements
p [1, -3, 5].sum   # => 3

# max and min
# Return the maximum or minimum element

p [1, -3, 5].min    # => -3
p [1, -3, 5].max    # => 5
p [].max            # => nil

# flatten
# Return the 1 dimensional version of any multidimensional array

multi_d = [
    [["a", "b"], "c"],
    [["d"], ["e"]],
    "f"
]

p multi_d.flatten   # => ["a", "b", "c", "d", "e", "f"]

=begin

symbols are immutable.
string can be "changed", but a symbol can never be "changed":

comparing two symbols is fast and efficient compared to regular strings.
If we don't intend to mutate the string, we can use a symbol to save some memory.
symbols are stored in exactly one memory location.
We're ensured the the identifier will remain intact, without change,
while also being efficient with memory.

=end

str = "hello"   # the string
sym = :hello    # the symbol

p str.length    # => 5
p sym.length    # => 5

p str[1]        # => "e"
p sym[1]        # => "e"

p str == sym    # => false
# a string is different from a symbol!

str = "hello"   # the string
sym = :hello    # the symbol

p str.length    # => 5
p sym.length    # => 5

p str[1]        # => "e"
p sym[1]        # => "e"

p str == sym    # => false
# a string is different from a symbol!

str = "hello"
sym = :hello

str[0] = "x"

# undefined method `[]=' for :hello:Symbol (NoMethodError)
# sym[0] = "x"

p str   # => "xello"
p sym   # => :hello

"hello".object_id   # => 70233443667980
"hello".object_id   # => 70233443606440
"hello".object_id   # => 70233443438700

:hello.object_id    # => 2899228
:hello.object_id    # => 2899228
:hello.object_id    # => 2899228

my_bootcamp = { :name=>"App Academy", :color=>"red", :locations=>["NY", "SF", "ONLINE"] }
p my_bootcamp           # => {:name=>"App Academy", :color=>"red", :locations=>["NY", "SF", "ONLINE"]}
p my_bootcamp[:color]   #=> "red

my_bootcamp = { name:"App Academy", color:"red", locations:["NY", "SF", "ONLINE"] }
p my_bootcamp           # => {:name=>"App Academy", :color=>"red", :locations=>["NY", "SF", "ONLINE"]}
p my_bootcamp[:color]   #=> "red


def method(arg_1, arg_2, *other_args)
    p arg_1         # "a"
    p arg_2         # "b"
    p other_args    # ["c", "d", "e"]
end

method("a", "b", "c", "d", "e")

def method(arg_1, arg_2, *other_args)
    p arg_1         # "a"
    p arg_2         # "b"
    p other_args    # []
end

method("a", "b")

# Avoid doing this, it's confusing:
def method(*other_args, required_arg)
    p other_args    # ["a", "b"]
    p required_arg  # "c"
end

method("a", "b", "c")

def greet(first_name, last_name)
    p "Hey " + first_name + ", your last name is " + last_name
end

names = ["grace", "hopper"]
# greet(names)    # ArgumentError: wrong number of arguments (given 1, expected 2)

def greet(first_name, last_name)
    p "Hey " + first_name + ", your last name is " + last_name
end

names = ["Grace", "Hopper"]
greet(*names)    # => "Hey Grace, your last name is Hopper"

arr_1 = ["a", "b"]
arr_2 = ["d", "e"]
arr_3 = [ *arr_1, "c", *arr_2 ]
p arr_3 # => ["a", "b", "c", "d", "e"]

old_hash = { a: 1, b: 2 }
new_hash = { **old_hash, c: 3 }
p new_hash # => {:a=>1, :b=>2, :c=>3}


# default act is the first element
p [11, 7, 2, 4].inject { |acc, el| acc + el } # => 24
p [11, 7, 2, 4].inject { |acc, el| acc * el } # => 616

# find minimum
x = [11, 7, 2, 4].inject do |acc, el|
    if el < acc
        el
    else
        acc
    end
end # => 2

p x

# result when you add all numbers in an array to 100
p [11, 7, 2, 4].inject(100) { |acc, el| acc + el } # => 124

# sums up all even numbers
[11, 7, 2, 4].inject(0) do |acc, el|
    if el.even?
        acc + el
    else
        acc
    end
end # => 6

def map_by_name(arr)
  arr.map {|hash| hash["name"]}
end

pets = [
  {"type"=>"dog", "name"=>"Rolo"},
  {"type"=>"cat", "name"=>"Sunny"},
  {"type"=>"rat", "name"=>"Saki"},
  {"type"=>"dog", "name"=>"Finn"},
  {"type"=>"cat", "name"=>"Buffy"}
]
print map_by_name(pets)
#=> ["Rolo", "Sunny", "Saki", "Finn", "Buffy"]
puts

countries = [
 {"name"=>"Japan", "continent"=>"Asia"},
 {"name"=>"Hungary", "continent"=>"Europe"},
 {"name"=>"Kenya", "continent"=>"Africa"},
]
print map_by_name(countries) #=> ["Japan", "Hungary", "Kenya"]
puts

def yell_sentence(sent)
  yelled = sent.split.map{|w| w.upcase + "!"}
  yelled.join(" ")
end

puts yell_sentence("I have a bad feeling about this")
#=> "I! HAVE! A! BAD! FEELING! ABOUT! THIS!"

def whisper_words(words)
  words.map {|w| w.downcase + "..."}
end

puts whisper_words(["KEEP", "The", "NOISE", "down"])
# => ["keep...", "the...", "noise...", "down..."]

def o_words(sentence)
  sentence.split(" ").select {|w| w.include?("o")}
end

puts o_words("How did you do that?") #=> ["How", "you", "do"]

def method(hash)
    p hash  # {"location"=>"SF", "color"=>"red", "size"=>100}
end

method({"location"=>"SF", "color"=>"red", "size"=>100})

# this also works:
method("location"=>"SF", "color"=>"red", "size"=>100)

def modify_string(str, options={"upper"=>false, "repeats"=>1})
    str.upcase! if options["upper"]
    p str * options["repeats"]
end

# less readable
modify_string("bye", {"upper"=>true, "repeats"=>3}) # => "BYEBYEBYE"

# more readable
modify_string("bye", "upper"=>true, "repeats"=>3)   # => "BYEBYEBYE"

modify_string("bye")   # => "bye"
modify_string("bye", "upper"=>true, "repeats"=>3)   # => "BYEBYEBYE"

# Scope

# Methods and Local Scope
# lexical scope.
# how variable names resolve if we put them in structures
# like methods, conditionals, or blocks

=begin
def say_hello
    message = "hello"
end

say_hello
p message   # NameError: undefined local variable

message = "hi"

def say_hello
    p message   # NameError: undefined local variable
end

say_hello

=end

# If we want something with global scope
# the variable must have a dollar at the start
$message = "hello globe"

def say_hello
    p $message
end

say_hello # => "hello globe"

def say_hello
    $message = "hello globe"
end


say_hello
p $message # => "hello globe"

# We can create a global variable inside
# and we can access it outside

def say_hello
    $message = "hello globe"
end

say_hello
p $message # => "hello globe"

# Ruby automatically defines some global variables for us to reference.
# For example, $PROGRAM_NAME will be a string describing the name of our program.
# U other global names like $stdin and $stdout handle user input and output.
# We can reference a $variable_name anywhere in our program because it is global!

# CONSTANTS

# A constant is denoted syntactically by beginning the name with a capital letter.
# By convention we like to make the entire name capital to emphasize it being a
# special constant.

FOOD = "pho"
p FOOD # => "pho"

FOOD = "ramen"  #warning: already initialized constant FOOD
                #warning: previous definition of FOOD was here

# You'll receive a warning when reassigning a constant.
# Reassignment means using = on that name again.
# A common point of confusion is that while you cannot reassign a constant,
# you can still mutate that constant name without warning:

FOODX = "pho"
FOODX[0] = "P"
p FOODX # => "Pho

# Constants will exist in global scope!

FOODY = "pho"
$drink = "ice coffee"

def my_favorite
    p FOODY
    p $drink
end

my_favorite

# we should use the global scope sparingly.
# We want to minimize our methods all referencing data that is outside of them,
# as manipulations to the data will be hard to track.
# Instead we should write methods that accept data as arguments
# as it is more explicit where the data is coming from.

# ====================================
# ====================================
# What does not have it's own scope?
# ====================================
# ====================================

# So methods and the global scope will be our primary structures that provide scope.
# Blocks don't have their own scope, they are really a part of the
# containing method's scope. Below, the times block can reference message.

# Other structures like conditionals or while loops also don't have their own scope,
# they are really part of the containing scope. Although a variable is defined within
# the if statement below, it is still accessible outside of the if statement,
# because if's don't have their own scope.

if true
    drink = "cortado"
end

p drink

# add element(s) to the end using push
people = ["Tommy", "Bex"]
p people.push("Maurice", "Abby")      # prints ["Tommy", "Bex", "Maurice", "Abby"]
p people                              # prints ["Tommy", "Bex", "Maurice", "Abby"]

# remove the last element using pop
people = ["Tommy", "Bex"]
p people.pop()                        # prints "Bex"
p people                              # prints ["Tommy"]

# add elements(s) to the front using unshift
people = ["Tommy", "Bex"]
p people.unshift("Oscar", "Matthias") # prints ["Oscar", "Matthias", "Tommy", "Bex"]
p people                              # prints ["Oscar", "Matthias", "Tommy", "Bex"]

# remove the first element using shift
people = ["Tommy", "Bex"]
p people.shift()                      # prints "Tommy"
p people                              # prints ["Bex"]

# check if an element exists in an array using include?
people = ["Tommy", "Bex", "Abby", "Maurice"]
p people.include?("Abby")   # prints true
p people.include?("Mashu")  # prints false

# find the index of an element in an array using index
people = ["Tommy", "Bex", "Abby", "Maurice"]
p people.index("Abby")      # prints 2
p people.index("Maurice")   # prints 3
p people.index("Oscar")     # prints nil
p people.index("Danny")     # prints nil

# convert a string into an array using split
sentence = "Hey Programmers! What's up."
p sentence.split(" ")      # prints ["Hey", "Programmers!", "What's", "up."]
p sentence.split("a")      # prints ["Hey Progr", "mmers! Wh", "t's up."]
p sentence.split("gram")   # prints ["Hey Pro", "mers! What's up."]
p sentence                 # prints "Hey Programmers! What's up."

# convert an array into a string using join
words = ["Rubies", "are", "red"]
p words.join(" ")          # prints "Rubies are red"
p words.join("-")          # prints "Rubies-are-red"
p words.join("HI")         # prints "RubiesHIareHIred"
p words                    # prints ["Rubies", "are", "red"]

people = ["Candace", "Jon", "Jose"]

# iterate over elements of an array using each
people.each { |person| puts person }
# Candace
# Jon
# Jose

# iterate over elements of an array with index using each_with_index
people.each_with_index do |person, i|
  puts person + i.to_s
end #
# Candace0
# Jon1
# Jose2

greeting = "hello"

# iterate over characters of a string using each_char
greeting.each_char { |char| print char + " " }
# h e l l o

# iterate over characters of a string with index using each_char.with_index
greeting.each_char.with_index do |char, i|
  puts char + i.to_s
end
# h0
# e1
# l2
# l3
# o4

# repeat a block using times
3.times do
  print "hi"
end
# hihihi

# specify a range of numbers using (start..end) or (start...end)

# including end
(2..6).each {|n| print n}  # 23456

# excluding end
(2...6).each {|n| print n} # 2345

hash = { "name" => "App Academy", "color" => "red" }

p hash["color"]  # prints "red"
p hash["age"]    # prints nil

k = "color"
p hash[k]        # prints "red"

hash["age"] = 5
p hash # prints {"name"=>"App Academy", "color"=>"red", "age"=>5}

hash = { "name" => "App Academy", "color" => "red" }

p hash.has_key?("name")             # prints true
p hash.has_key?("age")              # prints false
p hash.has_key?("red")              # prints false

p hash.has_value?("App Academy")    # prints true
p hash.has_value?(20)               # prints false
p hash.has_value?("color")          # prints false

hash = { "name" => "App Academy", "color" => "red" }

hash.each { |key, val| p key + ', ' + val} # prints
# "name, App Academy"
# "color, red"

hash.each_key { |key| p key } # prints
# "name"
# "color"

hash.each_value { |val| p val } # prints
# "App Academy"
# "red"

plain_hash = { }
plain_hash["city"] = "SF"

p plain_hash["city"]    # prints "SF"
p plain_hash["country"] # prints nil

hash_with_default = Hash.new("???")
hash_with_default["city"] = "NYC"

p hash_with_default["city"]    # prints "NYC"
p hash_with_default["country"] # prints "???"
