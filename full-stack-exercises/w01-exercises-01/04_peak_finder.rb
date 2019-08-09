# Write a method, peak_finder(arr), that accepts an array of numbers as an arg.
# The method should return an array containing all of "peaks" of the array.
# An element is considered a "peak" if it is greater than both it's left and right neighbor.
# The first or last element of the array is considered a "peak" if it is greater than it's one neighbor.

def peak_finder(arr)
  result = []
  # check if beginning is peak 
  result << arr[0] if arr[0] > arr[1]

  n = arr.length - 1
  
  (1...n).each do |i|
    result << arr[i] if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]
  end
  # check if end is peak 
  result << arr[-1] if arr[-1] > arr[-2]
  result
end

p peak_finder([1, 3, 5, 4])         # => [5]
p peak_finder([4, 2, 3, 6, 10])     # => [4, 10]
p peak_finder([4, 2, 11, 6, 10])    # => [4, 11, 10]
