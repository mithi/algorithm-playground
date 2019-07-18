require 'benchmark'
require 'test/unit'
include Test::Unit::Assertions

# Write a method that takes in a string of lowercase letters and
# spaces, producing a new string that capitalizes the first letter of
# each word.

def capitalize_words1(string)
  capitalized = ""
  isfirst = true

  string.each_char do |c|

    if c != " "
      if isfirst == false
        capitalized += c
        next
      end

      capitalized += c.upcase
      isfirst = false
      next
    end
    # c is a space, next c should be capitalized
    capitalized += c
    isfirst = true
  end

  capitalized
end


def capitalize_words2(string)
  string.split(" ").map {|word| word.capitalize}.join(" ")
end


def capitalize_words3(string)
  words = string.split(" ")
  i = 0

  while i < words.length
    words[i][0] = words[i][0].upcase
    i += 1
  end

  words.join(" ")
end


sentences = [
"Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.",
"The body may perhaps compensates for the loss of a true metaphysics.",
"She works two jobs to make ends meet; at least, that was her reason for not having time to join us.",
"If the Easter Bunny and the Tooth Fairy had babies would they take your teeth and leave chocolate for you?",
"If Purple People Eaters are real… where do they find purple people to eat?",
"A purple pig and a green donkey flew a kite in the middle of the night and ended up sunburnt.",
"Writing a list of random sentences is harder than I initially thought it would be.",
"There was no ice cream in the freezer, nor did they have money to go to the store.",
"What was the person thinking when they discovered cow’s milk was fine for human consumption… and why did they do it in the first place!?",
"I was very proud of my nickname throughout high school but today- I couldn’t be any different to what my nickname was.",
"Sometimes, all you need to do is completely make an ass of yourself and laugh it off to realise that life isn’t so bad after all.",
]

sentences.map! { |s| s.downcase }

sentences.each do |sentence|
  assert_equal capitalize_words1(sentence), capitalize_words2(sentence)
  assert_equal capitalize_words2(sentence), capitalize_words3(sentence)
  assert_equal capitalize_words1(sentence), capitalize_words3(sentence)
end

N = 10_000

puts "-----------------------"
puts "Benchmarks"
puts "-----------------------"
Benchmark.bm do |benchmark|

  benchmark.report("capitalize words 1") do
    N.times do
      sentences.each do |sentence|
        capitalize_words1 sentence
      end
    end
  end

  benchmark.report("capitalize words 2") do
    N.times do
      sentences.each do |sentence|
        capitalize_words2 sentence
      end
    end
  end

  benchmark.report("capitalize words 3") do
    N.times do
      sentences.each do |sentence|
        capitalize_words3 sentence
      end
    end
  end
end

=begin

        user     system      total        real
capitalize words 1  7.354480   0.011627   7.366107 (  7.388700)
capitalize words 2  1.680533   0.001673   1.682206 (  1.683787)
capitalize words 3  1.473380   0.001147   1.474527 (  1.475624)
=end

