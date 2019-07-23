# An abundant number is a number that is less than the sum of its divisors,
# not including itself.

# Ex. 12's divisors are 1, 2, 3, 4, 6, which sum to 16
# 16 > 12 so 12 is an abundant number.

# Write a function that takes a number and return true if the number is abundant
# otherwise, return false.


##################
def divisors(n)
  divs = []
  # NOT INCLUDING ITSELF
  (1...n).each do |i|
    if n % i == 0
      divs << i
    end
  end
  divs
end

def abundant?(num)
  divs = divisors(num)
  puts divs.to_s + " : " + divs.sum.to_s
  divs.sum > num
end

puts "-------Abundant-------"
puts abundant?(12) == true
puts abundant?(24) == true
puts abundant?(9) == false
puts abundant?(10001) == false
puts abundant?(20000) == true



# Save the Prisoner!
#
# A jail has n prisoners, and each prisoner has a unique ID number, ranging
# from 1 to n. There are m sweets that must be distributed to the prisoners.
# The jailer decides the fairest way to do this is by sitting the prisoners
# down in a circle (ordered by ascending ID number), and then, starting with
# some random prisoner, distribute one candy at a time to each sequentially
# numbered prisoner until all candies are distributed. For example, if the
# jailer picks prisoner ID=2, then his distribution order would be
# (2,3,4,5,...,n-1,n,1,2,3,4,...) until all m sweets are distributed.
#
# But wait — there's a catch — the very last sweet is poisoned! Can you find and
# print the ID number of the last prisoner to receive a sweet so they can be warned?
#
# n => Number of Prisoners
# m => Number of Sweets
# ID => Starting ID
# save_the_prisoner(N,M,ID)


def save_the_prisoner(n, m, id)
 prisoner_count = n
 sweet_count = m
 starting_prisoner = id

 poisoned = (starting_prisoner - 1 + sweet_count) % prisoner_count
 poisoned = poisoned != 0 ? poisoned : prisoner_count
end

puts "-------Save The Prisoners-------"
puts save_the_prisoner(5,2,1) == 2
puts save_the_prisoner(99, 99, 1) == 99
puts save_the_prisoner(49, 98, 2) == 1
puts save_the_prisoner(94431605, 679262176, 5284458) == 23525398

# Write a function that takes a string and
# returns a hash in which each key is a character in the string
# pointing to an array indicating the index that the character
# first occurs and last occurs.
#
# If the character occurs only once, the array should hold a single index
#
# Example:
#
# str = "banana"
# return {"b" => [0], "a" => [1, 5], "n" => [2, 4]}
# "b" occurs once at index 0
# "a" occurs three times, but the first is at index 1 and the last is at index 5
# "n" occurs three times, but the first is at index 2 and the last is at index 4

def first_last_indices(str)
  indices = Hash.new()

  (0...str.length).each do |i|
    c = str[i]
    if !indices.include?(c)
      indices[c] = [i]
    end
  end

  n = str.length - 1
  n.downto(0) do |i|

    c = str[i]
    if indices[c].length == 2
      next
    end

    if indices[c][0] != i
      indices[c] << i
    end
  end

  indices
end


puts "-------First Last Indices-------"
puts first_last_indices("cat") == {"c" => [0], "a" => [1], "t" => [2]}
puts first_last_indices("dude") == {"d" => [0, 2], "u" => [1], "e" => [3]}
puts first_last_indices("banana") == {"b" => [0], "a" => [1, 5], "n" => [2, 4]}
puts first_last_indices("racecar") == {"r" => [0, 6], "a" => [1, 5], "c" => [2, 4], "e" => [3]}

