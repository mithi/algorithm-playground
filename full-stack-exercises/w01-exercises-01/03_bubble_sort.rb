# Reimplement the bubble sort outlined in the preceding lecture.
# The bubble_sort method should accept an array of numbers and arrange the elements in increasing order.
# The method should return the array.
# Do not use the built-in Array#sort

def bubble_sort(arr)
  n = arr.length - 1

  while true
    sorted = true
    (0...n).each do |i|
      if arr[i] > arr[i + 1]
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
        sorted = false
      end
    end
    n -= 1
    break if sorted == true
  end
  arr
end

x = Array.new(20) { rand(1..30) }
p x
p bubble_sort(x)
p bubble_sort([2, 8, 5, 2, 6])      # => [2, 2, 5, 6, 8]
p bubble_sort([10, 8, 7, 1, 2, 3])  # => [1, 2, 3, 7, 8, 10]
p bubble_sort([1, 2, 3, 4, 5, 6, 7, 7, 8])