# Write a method that takes an integer `n` in; it should return
# n*(n-1)*(n-2)*...*2*1. Assume n >= 0.
# As a special case, `factorial(0) == 1`.
# Difficulty: easy
def factorial n

  if n <= 1
    return 1
  end

  x = 1
  n.downto 2 do |i|
    x *= i
  end
  x
end

# Write a method that will take a string as input, and return a new
# string with the same letters in reverse order
def reverse s
  r = ""
  (1..s.length).each do |i|
    r += s[-i]
  end
  r
end

# Write a method that takes in a string. Return the longest word in
# the string. You may assume that the string contains only letters and
# spaces. You may use the String `split` method to aid you in your quest.
def longest_word sentence
  words = sentence.split
  longest = ""
  length = 0

  words.each do |word|
    if word.length > length
      longest = word
      length = word.length
    end
  end
  longest
end

# Write a method that takes in an integer `num` and returns the sum of
# all integers between zero and num, up to and including `num`.
def sum_nums num
  sum = 0

  (1..num).each do |i|
    sum += i
  end
  sum
end

puts(sum_nums(9) == 45)

# Write a method that will take in a number of minutes, and returns a
# string that formats the number into `hours:minutes`.
def time_conversion minutes
  m = minutes / 60
  h = minutes - m * 60
  m.to_s + ":" + h.to_s
end


# Write a method that takes a string and returns the number of vowels
# in the string. You may assume that all the letters are lower cased.
# You can treat "y" as a consonant.
def count_vowels string
  vowels = ["a", "e", "i", "o", "u"]
  n = 0

  (0...string.length).each do |i|
    if vowels.include?(string[i])
      n += 1
    end
  end

  n
end


# Write a method that takes a string and returns true if it is a
# palindrome. A palindrome is a string that is the same whether written
# backward or forward. Assume that there are no spaces; only lowercase
# letters will be given.
def palindrome? string
  n = string.length / 2

  (0..n).each do |i|
    if string[i] != string[-(i + 1)]
      return false
    end
  end

  true
end

puts(reverse("Hello World") == "dlroW olleH")
puts(longest_word("the quick brown fox jumps over aaaaaaaaaaaaaHHHH the lazy dog") == "aaaaaaaaaaaaaHHHH")
puts(time_conversion(200) == "3:20")
puts(count_vowels("colour") == 3)


puts('palindrome?("abc") == false: ' + (palindrome?('abc') == false).to_s)
puts('palindrome?("abcba") == true: ' + (palindrome?('abcba') == true).to_s)
puts('palindrome?("z") == true: ' + (palindrome?('z') == true).to_s)
