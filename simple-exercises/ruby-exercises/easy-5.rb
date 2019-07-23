# ------------------------------------------------------------------------------
#
#
# In All Strings
# ------------------------------------------------------------------------------
# Check if a short_string is a substring of ALL of the long_strings

def in_all_strings?(long_strings, short_string)
  # sliding window

  # check each long_string
  long_strings.each do |s|
    in_string = false
    n = s.length - short_string.length

    # check each substring of a long string
    # if equal to short string
    (0..n).each do |i|
      # if we encounter the shortstring in the substring
      # then we should move on to the next long string
      if s.slice(i, short_string.length) == short_string
        in_string = true
        break
      end
    end
    # if we didn't find a substring in this long string
    # then we know that not all substrings are in the long string
    if in_string == false
      return false
    end
  end

  true
end

puts "---------In All Strings-------"
puts in_all_strings?(["thisisaverylongstring", "thisisanotherverylongstring"], "sisa") == true
puts in_all_strings?(["thisisaverylongstring", "thisisanotherverylongstring"], "isan") == false
puts in_all_strings?(["gandalf", "aragorn", "sauron"], "sam") == false
puts in_all_strings?(["axe", "ajax", "axl rose"], "ax") == true


# Biodiversity
# ------------------------------------------------------------------------------
# Given an array of specimens, return the biodiversity index, which is defined
# by the following formula: number_of_species^2 times the smallest_population_size
# divided by the largest_population_size.

# In code, biodiversity = number_of_species**2 * smallest_population_size / largest_population_size
#
# ------------------------------------------------------------------------------

#
def find_minmax(populations)
  min, max = nil, nil

  populations.each do |s, p|
    if min == nil or p < min
      min = p
    end

    if max == nil or p > max
      max = p
    end
  end

  [min, max]
end

def biodiversity_index(specimens)

  # put speciments to hashmap
  populations = Hash.new(0)
  specimens.each do |s|
    populations[s] += 1
  end

  min, max = find_minmax(populations)
  bio = populations.count**2 * min / max
  bio
end

puts "------Biodiversity------"
puts biodiversity_index(["cat"]) == 1
puts biodiversity_index(["cat", "cat", "cat"]) == 1
puts biodiversity_index(["cat", "cat", "dog"]) == 2
puts biodiversity_index(["cat", "fly", "dog"]) == 9
puts biodiversity_index(["cat", "fly", "dog", "dog", "cat", "cat"]) ==


# Censor
# ------------------------------------------------------------------------------
# Write a function censor(sentence, curse_words) that censors the words given.
# Replace the vowels in the curse word with "*".

def asterisked(word)
  vowels = ["a", "e", "i", "o", "u"]
  new_word = ""
  word.each_char do |c|
    if vowels.include?(c)
      new_word << "*"
    else
      new_word << c
    end
  end
  new_word
end

def censor(sentence, curse_words)
  words = sentence.split(" ")
  new_words = []

  words.each do |word|

    if curse_words.include?(word.downcase)
      new_words << asterisked(word)
    else
      new_words << word
    end
  end
  new_words.join(" ")
end


puts "------Censor------"
puts censor("Darn you Harold you son of a gun", ["darn", "gun"]) == "D*rn you Harold you son of a g*n"
puts censor("Schnikeys I don't give a diddly squat", ["schnikeys", "diddly", "squat"]) == "Schn*k*ys I don't give a d*ddly sq**t"

# For F's Sake
# ------------------------------------------------------------------------------
# Given a string, return the word that has the letter "f" closest to
# the end of it.  If there's a tie, return the earlier word.  Ignore punctuation.
#
# If there's no f, return an empty string.
# ------------------------------------------------------------------------------


def for_fs_sake(string)
  words = string.split(" ")
  the_word = ""
  f_index = nil # index from end

  words.each do |word|
    #find an f
    (1..word.length).each do |i|
      if word[-i] == "f"
        if the_word == "" or i < f_index
          the_word = word
          f_index = i
          break
        end
      end
    end
  end

  the_word
end

puts "------For F's Sake------"
puts for_fs_sake("puff daddy") == "puff"
puts for_fs_sake("I got a lot of problems with you people! And now you're gonna hear about it!") == "of"
puts for_fs_sake("fat friars fly fish") == "fat"
puts for_fs_sake("the French call him David Plouffe") == "Plouffe"
puts for_fs_sake("pikachu! i choose you!") == ""
