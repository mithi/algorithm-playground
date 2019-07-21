# Write a method that returns the `n`th prime number. Recall that only
# numbers greater than 1 can be prime.

def is_prime?(n)
  if n == 2
    return true
  end

  (2...n).each do |i|
    if n % i == 0
      return false
    end
  end
  true
end


def nth_prime(n)
  if n < 2
    return false
  end

  x = 2 # store prime here
  i = 0 # ith prime counter

  while true
    if is_prime?(x)
      # increment i, this is ith prime
      i+=1
      if i == n
        return x
      end
    end
    # evaluate next number
    x+=1
  end
end


# Write a method that takes a string in and returns true if the letter
# "z" appears within three letters **after** an "a". You may assume
# that the string contains only lowercase letters.
def nearby_az string

  (0...string.length).each do |i|
    if string[i] == "a"
      if string[(i + 1)..(i + 3)].include?("z")
        return true
      end
    end
  end
  false
end

# Write a method that takes an array of numbers. If a pair of numbers
# in the array sums to zero, return the positions of those two numbers.
# If no pair of numbers sums to zero, return `nil`.

#brute force
def two_sum_brute nums
  (0...nums.length).each do |i|
    ((i + 1)...nums.length).each do |j|
      if nums[i] + nums[j] == 0
        return i, j
      end
    end
  end
  nil
end


# one pass with hashmap
def two_sum nums
  # nums[index] : index
  map = {}

  nums.each_with_index do |n, i|
    if map[-n]
      return map[-n], i
    end
    map[n] = i
  end
  nil
end

# Write a method that takes an array of numbers in. Your method should
# return the third greatest number in the array. You may assume that
# the array has at least three numbers in it.
def third_greatest(nums)
  first, second, third = nil, nil, nil

  nums.each do |n|
    if first == nil or n > first
      first, second, third = n, first, second
    elsif second == nil or n > second
      second, third = n, second
    elsif third == nil or n > third
      third = n
    end
  end
  third
end

# Write a method that takes in a string. Your method should return the
# most common letter in the array, and a count of how many times it
# appears.
def most_common_letter(string)
  # letter : how many times
  letter_count = Hash.new(0)

  (0...string.length).each do |i|
    letter_count[string[i]] += 1
  end

  letter = string[0]
  count = letter_count[letter]

  (1...string.length).each do |i|
    if letter_count[string[i]] > count
      count = letter_count[string[i]]
      letter = string[i]
    end
  end

  [letter, count]
end

# Write a method that takes in a number and returns a string, placing
# a single dash before and after each odd digit. There is one
# exception: don't start or end the string with a dash.
# You may wish to use the `%` modulo operation; you can see if a number
# is even if it has zero remainder when divided by two.
def dasherize_number(num)
  number = num.to_s
  dashed = ""

  dashed = number[0]
  if number[0].to_i % 2 == 1
    dashed += "-"
  end

  number[1..-1].each_char do |n|

    if n.to_i % 2 == 1
      if dashed[-1] != "-"
        dashed = dashed + "-" + n + "-"
      else
        dashed += n
      end
    else
      dashed += n
    end
  end

  if dashed[-1] == "-"
    return dashed[0...-1]
  end

  dashed
end

# Write a method that takes in a string and an array of indices in the
# string. Produce a new string, which contains letters from the input
# string in the order specified by the indices of the array of indices.

def scramble_string(string, positions)
  letters = ""

  positions.each do |i|
    letters += string[i]
  end

  letters
end

