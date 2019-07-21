


def palindrome?(string)

  n = string.length / 2

  (0...n).each do |i|
    if string[i] != string[-(i + 1)]
      return false
    end
  end
  true
end

# Write a method that takes in a string of lowercase letters (no
# uppercase letters, no repeats). Consider the *substrings* of the
# string: consecutive sequences of letters contained inside the string.
# Find the longest such string of letters that is a palindrome.
#
# Note that the entire string may itself be a palindrome.
#
# You may want to use Array's `slice(start_index, length)` method,
# which returns a substring of length `length` starting at index
# `start_index`:

def longest_palindrome(string)
  if string.length <= 1
    return string
  end

  i = 0
  string.length.downto(1).each do |length|
    # .. is inclusive
    (0..i).each do |start_index|
      if palindrome?(string.slice(start_index, length))
        return string.slice(start_index, length)
      end
    end

    i += 1
  end

  string[0]
end

# Write a method that takes in two numbers. Return the greatest
# integer that evenly divides both numbers. You may wish to use the
# `%` modulo operation.


def greatest_common_factor(number1, number2)
  # get the smaller number
  n = number1 < number2 ? number1 : number2

  # check each number i
  # starting from this number n down to 1
  # if it divides both number1 and number2 evenly
  # if so, then this is the gcd
  n.downto(1).each do |i|
    if number1 % i == 0 and number2 % i == 0
      return i
    end
  end
  1
end

# Write a method that takes in a string and returns the number of
# letters that appear more than once in the string. You may assume
# the string contains only lowercase letters. Count the number of
# letters that repeat, not the number of times they repeat in the
# string.

def num_repeats(string)

  # number of repeating characters
  n = 0
  # tracks the character frequency
  repeats = Hash.new(0)

  string.each_char do |c|
    repeats[c] += 1
    if repeats[c] == 2
      n += 1
    end
  end
  n
end

puts('num_repeats("abdbc") == 1: ' + (num_repeats('abdbc') == 1).to_s)
puts('num_repeats("aaa") == 1: ' + (num_repeats('aaa') == 1).to_s)
puts('num_repeats("abab") == 2: ' + (num_repeats('abab') == 2).to_s)
puts('num_repeats("cadac") == 2: ' + (num_repeats('cadac') == 2).to_s)
puts('num_repeats("abcde") == 0: ' + (num_repeats('abcde') == 0).to_s)
