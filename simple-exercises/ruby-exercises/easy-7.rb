# 13 - 17 minutes

# Define a method that returns the sum of all the non-negative integers up to and including its argument.
# sum_to(3) => 6
def sum_to(int)
  if int <= 0
    return 0
  end

  sum = 0
  (1..int).each do |i|
    sum += i
  end

  sum
end

# Define a method, #e_words(str), that accepts a string as an argument. Your method return the number of words in the string that end with the letter "e".
# e_words("tree") => 1
# e_words("Let be be finale of seem.") => 3
def e_words(str)
  words = str.split(" ")
  e = 0

  words.each do |word|
    chars = word.split("")
    if chars.include?("e")
      e += 1
    end
  end
  e
end

# A magic number is a number whose digits, when added together, sum to 7, e.g., 34. Define a method that returns an array of the first n magic numbers. You may wish to write a helper method (magic_number?) that returns a boolean indicating whether a number is magic. This problem is harder than anything you'll receive on the coding assessment.
# magic_numbers(3) => [7, 16, 25]
def magic_number?(n)
  # convert # to string
  string = n.to_s
  number = 0
  # sum each number
  string.each_char do |s|
    number += s.to_i
  end

  number == 7
end

def magic_numbers(n)
  if n <= 0
    return []
  end

  test_number = 7
  i = 0
  numbers = []

  while true
    if magic_number?(test_number)
      i += 1
      numbers << test_number
      if i == n
        return numbers
      end
    end
    test_number += 1
  end
  # should not happen
end

# DO NOT MODIFY CODE BELOW

$success_count = 0
$failure_count = 0

def deep_dup(arr)
  arr.inject([]) { |acc, el| el.is_a?(Array) ? acc << deep_dup(el) : acc << el }
end

def note_success(returned, invocation, expectation)
  puts "success: #{invocation} => #{expectation}"
  $success_count += 1
end

def note_failure(returned, invocation, expectation)
  puts "failure: #{invocation}: expected #{expectation}, returned #{returned}"
  $failure_count += 1
end

def format_args(args)
  o_args = deep_dup(args)
  o_args.map! do |arg|
    arg = prettify(arg)
    arg.class == Array ? arg.to_s : arg
  end
  o_args.join(', ')
end

def prettify(statement)
  case statement
  when Float
    statement.round(5)
  when String
    "\"#{statement}\""
  when NilClass
    "nil"
  else
    statement
  end
end

def equality_test(returned, invocation, expectation)
  if returned == expectation && returned.class == expectation.class
    note_success(returned, invocation, expectation)
  else
    note_failure(returned, invocation, expectation)
  end
end

def identity_test(returned, invocation, expectation, args)
  if returned.__id__ == args[0].__id__
    equality_test(returned, invocation, expectation)
  else
    puts "failure: #{invocation}: You did not mutate the original array!"
    $failure_count += 1
  end
end

def method_missing(method_name, *args)
  method_name = method_name.to_s
  expectation = args[-1]
  args = args[0...-1]
  if method_name.start_with?("test_")
    tested_method = method_name[5..-1]
    print_test(tested_method, args, expectation)
  else
    method_name = method_name.to_sym
    super
  end
end

def print_test(method_name, args, expectation)
  returned = self.send(method_name, *args)
  returned = prettify(returned)
  expectation = prettify(expectation)
  args_statement = format_args(args)
  invocation = "#{method_name}(#{args_statement})"
  method_name.include?("!") ? identity_test(returned, invocation, expectation, args) : equality_test(returned, invocation, expectation)
  rescue Exception => e
    puts "failure: #{invocation} threw #{e}"
    puts e.backtrace.select {|t| !t.include?("method_missing") && !t.include?("print_test")}
    $failure_count += 1
end

puts "
sum_to:
" + "*" * 15 + "
"
test_sum_to(3, 6)
test_sum_to(0, 0)
puts "
e_words:
" + "*" * 15 + "
"
test_e_words("loom", 0)
test_e_words("To be or not to be", 2)
puts "
magic_numbers:
" + "*" * 15 + "
"
test_magic_numbers(3, [7, 16, 25])
test_magic_numbers(0, [])
puts
puts "TOTAL CORRECT: #{$success_count} / #{$success_count + $failure_count}"
puts "TOTAL FAILURES: #{$failure_count}"
$success_count = 0
$failure_count = 0
