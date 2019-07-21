# Word With Most Repeats
# ------------------------------------------------------------------------------
# Given a sentence, find which word has the greatest amount of repeated letters.
#
# For example, "I took the road less traveled and that has made all the difference"
# should return "difference" because it has two repeated letters (f and e).
#
# All words will be separated by spaces and there will be no punctuation or
# capitalization.  If there is a tie return the first word.  It doesn't matter
# how many times individual letters repeat, just that they repeat (see the third test
# case).

def count_repeated_letters(word)
  # character: # of occurences
  occurences = Hash.new(0)
  count = 0

  word.each_char do |c|
    occurences[c] += 1
    if occurences[c] == 2
      count+=1
    end
  end
  count
end

def word_with_most_repeats(sentence)

  words = sentence.split(" ")
  best_word = words[0]
  count = count_repeated_letters(words[0])

  words[1..-1].each do |word|
    current_count = count_repeated_letters(word)
    if current_count > count
      count = current_count
      best_word = word
    end
  end
  best_word
end

puts "-------Word With Most Repeats-------"
puts word_with_most_repeats('good luck') == 'good'
puts word_with_most_repeats('what if there is a tie betwixt words') == 'there'
puts word_with_most_repeats('ooooooooooh tutu') == 'tutu'

# Isogram Matcher
# ------------------------------------------------------------------------------
# An isogram is a word with only unique, non-repeating letters. Given two isograms
# of the same length, return an array with two numbers indicating matches:
# the first number is the number of letters matched in both words at the same position,
# and the second is the number of letters matched in both words but not in the
# same position.

def has_letter(c, word)
  word.each_char do |i|
    if i == c
      return true
    end
  end
  false
end

def isogram_matcher(isogram1, isogram2)
  #
  # your code goes here
  #
  same_position = 0
  other_position = 0

  (0...isogram1.length).each do |i|
    if isogram1[i] == isogram2[i]
      same_position += 1
    elsif has_letter(isogram2[i], isogram1)
      other_position += 1
    end
  end
  [same_position, other_position]
end

puts "-------Isogram Matcher-------"
puts isogram_matcher("an", "at") == [1, 0]
puts isogram_matcher("or", "go") == [0, 1]
puts isogram_matcher("cat", "car") == [2, 0]
puts isogram_matcher("cat", "tap") == [1, 1]
puts isogram_matcher("home", "dome") == [3, 0]
puts isogram_matcher("gains", "snake") == [0, 3]
puts isogram_matcher("glamourize", "blueprints") == [1, 4]
puts isogram_matcher("ultrasonic", "ostracized") == [3, 4]
puts isogram_matcher("unpredictably", "hydromagnetic") == [1, 8]


# Xbonacci
# ------------------------------------------------------------------------------

# Write a Xbonacci function that works similarly to the fibonacci sequence.
# The fibonacci sequence takes the previous two numbers in the sequence and adds
# them together to create the next number.
#
# First five fibonacci numbers = [1, 1, 2, 3, 5]
# The fourth fibonacci number (3) is the sum of the two numbers before it
# (1 and 2).
#
# In Xbonacci, the sum of the previous X numbers (instead of the previous 2 numbers)
# of the sequence becomes the next number in the sequence.
#
# The method will take two inputs: the starting sequence with X number of
# elements and an integer N, and return the first N elements in the given
# sequence.  Take a look at the test cases for examples.
#
# In the code, how_many_numbers_to_sum is the same as X (name your variables
# descriptively!).
#
# In the code, number_of_fibonacci_numbers_to_return is the same as N.

def xbonacci(starting_sequence, number_of_xbonacci_numbers_to_return)
  sequence = starting_sequence
  # length of array to return
  n = number_of_xbonacci_numbers_to_return
  # numbers of elements before to sum
  x = starting_sequence.length
  # numbers to add to array
  i = n - x
  (0...i).each do |i|
    s = sequence[i...(x + i)].sum
    sequence << s
  end

  sequence
end

puts "-------Xbonacci-------"
puts xbonacci([1, 1], 5) == [1, 1, 2, 3, 5]
puts xbonacci([1, 1, 1], 6) == [1, 1, 1, 3, 5, 9]
puts xbonacci([1, 1, 1, 1], 8) == [1, 1, 1, 1, 4, 7, 13, 25]
puts xbonacci([1, 1, 1, 1, 1, 1], 10) == [1, 1, 1, 1, 1, 1, 6, 11, 21, 41]
puts xbonacci([0, 0, 0, 0, 1], 10) == [0, 0, 0, 0, 1, 1, 2, 4, 8, 16]


#  Cupcake Solver
#------------------------------------------------------------------------------
# It's Jennifer's birthday today. Jennifer's mom decided to bake different kinds
# of cupcakes for Jennifer's first grade class.  Everybody needs to have an equal
# amount of the different kinds of cupcakes.

# Write a method that takes an array of the counts of the different kinds of
# cupcakes and the number of students in the class, and returns
# the total number of cupcakes that each student in the class
# should get.

# Every student should have equal amounts of the same kind of cupcake.
# No student gets to have more cupcakes than the others.  There can be leftover
# cupcakes.

# An array of [1, 2, 3] means that there's one red velvet cupcake,
# two vanilla cupcakes, and three chocolate cupcakes.

# Example: cupcake_solver([10, 10, 10], 5) == 6  means that there are five
# students in the class, and each student gets to eat six cupcakes, total.


def cupcake_solver(cupcake_counts, number_of_students_in_class)
  # number of cupcakes for each flavor
  cake_set = cupcake_counts
  n = number_of_students_in_class
  cakes_per_student = 0

  cake_set.each do |count|
    # cakes per student for this flavor
    c = count / n
    # running total
    cakes_per_student += c
  end
  cakes_per_student
end


puts "-------Cupcake Solver-------"
puts cupcake_solver([10, 10, 10], 5) == 6
puts cupcake_solver([25, 27, 30], 5) == 16
puts cupcake_solver([32, 27, 28], 20) == 3
puts cupcake_solver([32, 27, 28, 24], 20) == 4


=begin

-------Word With Most Repeats-------
true
true
true
-------Isogram Matcher-------
true
true
true
true
true
true
true
true
true
-------Xbonacci-------
true
true
true
true
true
-------Cupcake Solver-------
true
true
true
true
=end
