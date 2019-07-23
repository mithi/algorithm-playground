# 45 minutes

# Price is Right
# ------------------------------------------------------------------------------
# Given a list of bids and an actual retail price, return the bid that is closest
# to the actual retail price without going over that price.
#
# Assume there is always at least one bid below the retail price.

def price_is_right(bids, actual_retail_price)

  best_bid = nil
  smallest_diff = nil

  bids.each do |bid|
    diff = actual_retail_price - bid

    if diff > 0
      if best_bid == nil or smallest_diff > diff
        smallest_diff = diff
        best_bid = bid
      end
    end
  end
  best_bid
end

puts "-------Price is Right-------"
puts price_is_right([200, 2350, 1400, 1600], 1599) == 1400
puts price_is_right([950, 850, 1000, 1], 1300) == 1000


# Total Product Sequence
# ------------------------------------------------------------------------------
# The total product sequence starts with [1, 2, 3] as a "base case" (what you
# start with).  The next number in the sequence is the product of all the numbers
# before it.  Given a number n, find the nth number of the total product sequence.
#
# Assume n must be at least 1

def total_product_sequence(n)
  if n < 4
    return n
  end

  product = 6

  (4..n).each do |i|
    if i == n
      return product
    end
    product *= product
  end
end

puts "-------Total Product Sequence-------"
puts total_product_sequence(1) == 1
puts total_product_sequence(2) == 2
puts total_product_sequence(3) == 3
puts total_product_sequence(4) == 6 # 3 * 2 * 1
puts total_product_sequence(5) == 36 # 6 * 3 * 2 * 1
puts total_product_sequence(6) == 1296 # 36 * 6 * 3 * 2 * 1
puts total_product_sequence(8) == 2821109907456 # etc...


# Products Except Me
# ------------------------------------------------------------------------------
#
# Given an array of numbers, calculate all the different products that remain when
# you take each element out of the array.
#
# Examples:
#
# [2, 3, 4] => [12, 8, 6], where:
#   12 because you take out 2, leaving 3 * 4
#   8, because you take out 3, leaving 2 * 4
#   6, because you take out 4, leaving 2 * 3
# ]
#
# [1, 2, 3, 5] => [30, 15, 10, 6], where:
#   30 because you take out 1, leaving 2 * 3 * 5
#   15, because you take out 2, leaving 1 * 3 * 5
#   10, because you take out 3, leaving 1 * 2 * 5
#   6, because you take out 5, leaving 1 * 2 * 3
# ]
#
#
#

def products_except_me(numbers)
  # get the products of all numbers
  product = 1
  numbers.each do |i|
    product *= i
  end

  results = []
  # remove the element in product by dividing
  numbers.each do |i|
    results << (product / i)
  end
  results
end

puts "-------Products Except Me-------"
puts products_except_me([2, 3, 4]) == [12, 8, 6]
puts products_except_me([1, 2, 3, 5]) == [30, 15, 10, 6]
puts products_except_me([7, 2, 1, 4]) == [8, 28, 56, 14]


# More than N Factors
# ------------------------------------------------------------------------------
# Given an array of numbers, return all the numbers that have at least N
# factors (including 1 and itself as factors).

# For example, if you were given [1, 3, 10, 16] and wanted to find the numbers
# that had at least five factors, you would return [16] because 16 has five
# factors (1, 2, 4, 8, 16) and the others have fewer than five factors.

def number_of_factors(n)
  # bruteforce, simplest
  # least efficient way
  count = 0

  (1..n).each do |i|
    if n % i == 0
      count += 1
    end
  end

  count
end

def more_than_n_factors(numbers, n)
  # n must be atleast 1
  if n < 1
    return nil
  end
  # all numbers have atleast one factor
  if n == 1
    return numbers
  end

  results = []

  numbers.each do |number|
    if number_of_factors(number) >= n
      results << number
    end
  end
  results
end

puts "-------More Than N Factors-------"
puts more_than_n_factors([1, 3, 10, 16], 5) == [16]
puts more_than_n_factors([1, 3, 10, 16], 2) == [3, 10, 16]
puts more_than_n_factors([20, 36, 39, 16], 6) == [20, 36]


# One-week Wonders
# ------------------------------------------------------------------------------
# Given a list of songs at the top of the charts, return the songs that only
# stayed on the chart for a week at a time.
#
# Songs CAN reappear on the chart, as long as it's for a week at a time. Only
# count those songs once.
#
# Suggested strategy: find the songs that show up multiple times in a row and
# subtract them out.


def one_week_wonders(songs)
  wonders = []
  (1...(songs.length - 1).each do |i|
    # two conditions must be satisfied
    # for it NOT to be a one week wonder
    # song this week is the song from previous week
    # or song this week is the song next week
    if songs[i - 1] == songs[i] or songs[i] == songs[i + 1]
      # if it's already in the not wonders, lets not repear ourselves
      if !not_wonders.include?(songs[i])
        not_wonders << songs[i]
      end
    end
  end

  wonders = []
  songs.each do |song|
    # if it is not in the not_wonders list then it is a wonder
    # we should add a song that is already in the wonders list
    if !not_wonders.include?(song) and !wonders.include?(song)
      wonders << song
    end
  end

  wonders
end

top_hits_1 = ["Call Me Maybe", "Protect Ya Neck", "Call Me Maybe", "Protect Ya Neck", "Protect Ya Neck"]
one_week_wonders_1 = ["Call Me Maybe"]

top_hits_2 = ["Beat It", "Beat It", "Careless Whisper", "Beat It", "Baby", "Baby", "Never Gonna Give You Up", "Uptown Funk", "Uptown Funk", "Uptown Funk"]
one_week_wonders_2 = ["Careless Whisper", "Never Gonna Give You Up"]

puts "-------One Week Wonders-------"
puts one_week_wonders(top_hits_1) == one_week_wonders_1
puts one_week_wonders(top_hits_2) == one_week_wonders_2
