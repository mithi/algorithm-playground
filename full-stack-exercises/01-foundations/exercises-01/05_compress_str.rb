# Write a method, compress_str(str), that accepts a string as an arg.
# The method should return a new str where streaks of consecutive characters are compressed.
# For example "aaabbc" is compressed to "3a2bc".

def compress_str(string)
  
  result = ""
  current = string[0]
  count = 1 

  string[1..-1].each_char do |c|
    if c == current
      count += 1
    else
      result << count.to_s if count > 1
      result << current
      count = 1
      current = c
    end
  end

  result << count.to_s if count > 1
  result << current
  result
end

p compress_str("aaabbc")        # => "3a2bc"
p compress_str("xxyyyyzz")      # => "2x4y2z"
p compress_str("qqqqq")         # => "5q"
p compress_str("mississippi")   # => "mi2si2si2pi"
