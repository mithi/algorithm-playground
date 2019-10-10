# The count-and-say sequence is the sequence of integers with the first five terms as following:
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
# Note: Each term of the sequence of integers will be represented as a string.

def count_until_change(s, i)
  nil if i >= s.length or i < 0

  ch = s[i]
  substring = s[i..-1]
  substring.each_char.inject(0) do |count, current|
    return count if current != ch
    count + 1
  end
end

def build_say(string)
  result = ""
  i = 0
  loop do
    count = count_until_change(string, i)
    result += "#{count}#{string[i]}"
    i += count
    return result if i >= string.length
  end
end

def count_and_say(n)
  result = "1"

  (n - 1).times do
    result = build_say(result)
  end
  result
end

puts "#{count_until_change("1", 0)} == 1"
puts "#{count_until_change("1211", 1)} == 1"
puts "#{count_until_change("1211", 2)} == 2"
puts "#{count_until_change("13112221", 0)} == 1"
puts "#{count_until_change("13112221", 1)} == 1"
puts "#{count_until_change("13112221", 2)} == 2"
puts "#{count_until_change("13112221", 4)} == 3"

puts build_say("1") == "11"
puts build_say("11") == "21"
puts build_say("21") == "1211"
puts build_say("1211") == "111221"
puts build_say("111221") == "312211"
puts build_say("312211") == "13112221"
puts build_say("13112221") == "1113213211"

puts count_and_say(1) == "1"
puts count_and_say(2) == "11"
puts count_and_say(3) == "21"
puts count_and_say(4) == "1211"
puts count_and_say(5) == "111221"
