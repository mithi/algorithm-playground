# Completed in 14 minutes

# Write a function lucky_sevens?(numbers), which takes in an array of integers
# and returns true if any three consecutive elements sum to 7

def lucky_sevens?(nums)
  if nums.length < 3
    return false
  end

  n = nums.length - 3
  # .. is inclusive
  (0..n).each do |i|
    if nums[i...(i+3)].sum == 7
      return true
    end
  end
  false
end

puts lucky_sevens?([2,1,5,1,0]) == true # => 1 + 5 + 1 == 7
puts lucky_sevens?([0,-2,1,8]) == true # => -2 + 1 + 8 == 7
puts lucky_sevens?([7,7,7,7]) == false
puts lucky_sevens?([3,4,3,4]) == false

#oddball_sum
#Write a function oddball_sum(numbers),
# which takes in an array of integers and
# returns the sum of all the odd elements.

def oddball_sum(nums)
  odd_sum = 0

  nums.each do |n|
    if n % 2 == 1
      odd_sum += n
    end
  end
  odd_sum
end

puts oddball_sum([1,2,3,4,5]) == 9 # => 1 + 3 + 5 == 9
puts oddball_sum([0,6,4,4]) == 0
puts oddball_sum([1,2,1]) == 2


# Write a function disemvowel(string), which takes in a string,
# and returns that string with all the vowels removed.
# Treat “y” as a consonant.

# not all characters are lowercase
def disemvowel(string)
  vowels = ['a', 'e', 'i', 'o', 'u']
  new_string = ""

  string.each_char do |c|
    # if this character is not a vowel
    if !vowels.include?(c.downcase)
      new_string += c
    end
  end
  new_string
end

puts disemvowel("foobar") == "fbr"
puts disemvowel("ruby") == "rby"
puts disemvowel("aeiou") == ""


# Anagrams are two words with the exact same letters.
# Write a function that take two strings and returns true if they are anagrams
# and false if they are not.

def anagrams?(str1, str2)
  if str1.length != str2.length
    return false
  end

  chars1 = str1.split("")
  chars2 = str2.split("")

  c1counts = Hash.new(0)
  c2counts = Hash.new(0)

  # make character freq table
  (0...str1.length).each do |i|
    c1, c2 = chars1[i], chars2[i]
    c1counts[c1] += 1
    c2counts[c2] += 1
  end

  if c1counts.count != c2counts.count
    return false
  end

  c1counts.each do |k, v|
    if c2counts[k] != v
      return false
    end
  end

  true
end

puts "-------Anagrams-------"
puts anagrams?("alert", "alter") == true
puts anagrams?("desert", "rested") == true
puts anagrams?("banana", "fofanna") == false
puts anagrams?("meat master", "team stream") == true


# Write a method, #build_power_plants, that will take in two arguments. The
# first of which is the number of cities that need to be powered. The cities
# are arranged in a line and are equidistant from eachother.
#   The second argument will be the range of each powerplant (the number of cities
# in each direction a plant can reach and power). So, a range of 1 means that each
# plant can only reach the cities on either side of it. A range of 0 means that the
# plants can only power the city they are built in.
#
#   Your method should dictate which cities' powerplants need to be built such
# that all of the cities have power, and the least number of cities have powerplants
# as possible.
#
#   Output an array of the cities, with 0 representing a city without a powerplant
# and 1 representing a city with one.
#
# For example:
# build_power_plants(3, 2) means that there are three cities, and each powerplant
# will have a range of two cities. Therefore your method should output the array
# { 0, 1, 0 ]


def build_power_plants(number_of_cities, plant_range)
  if number_of_cities == 0
    return []
  end

  # [1, 1, 1...]
  if plant_range == 0
    return Array.new(number_of_cities, 1)
  end


  results = Array.new(number_of_cities, 0)
  diameter = 2 * plant_range + 1
  row = 0

  # plant_range = 3, # cities = 17
  # diameter = 2 * plant_range + 1
  #  0,  1,  2,  3,  4,  5,  6   => first_index   = 0 * 7
  #              1               => current_plant = 0 + 3 = 3
  #  7,  8,  9, 10, 11, 12, 13   => first_index   = 1 * 7
  #             1                => current_plant = 7 + 3 = 10
  # 14, 15, 16                   => first_index   = 2 * 7 = 14
  #         1                    => current_plant = 17 >= #cities
                                 # so current_plant = #cities - 1 = 16(last index)

  while true
    first_index = row * diameter

    # row doesnt exist
    if first_index >= number_of_cities
      return results
    end

    current_plant = first_index + plant_range

    # plant spot doesn't exist
    # put plant on the last city instead
    if current_plant >= number_of_cities
      results[-1] = 1
      return results
    end

    results[current_plant] = 1
    row += 1 # next row
  end

end

puts "-------Power Plants-------"
puts build_power_plants(0,1) == []#
puts build_power_plants(1,1) == [1]#
puts build_power_plants(1,4) == [1]#
puts build_power_plants(2,1) == [1, 0] || build_power_plants(2,1) == [0, 1]#
puts build_power_plants(2,0) == [1, 1]#
puts build_power_plants(3,0) == [1, 1, 1] #

puts build_power_plants(3,1) == [0, 1, 0] #

puts build_power_plants(3,2) == [1, 0, 0] || #
  build_power_plants(3,2) == [0, 1, 0] ||
  build_power_plants(3,2) == [0, 0, 1]

puts build_power_plants(5,1) == [0, 1, 0, 1, 0] ||
  build_power_plants(5,1) == [1, 0, 0, 1, 0] ||
  build_power_plants(5,1) == [0, 1, 0, 0, 1]

puts build_power_plants(5,2) == [0, 0, 1, 0, 0]
puts build_power_plants(10, 2) == [0, 0, 1, 0, 0, 0, 0, 1, 0, 0]
