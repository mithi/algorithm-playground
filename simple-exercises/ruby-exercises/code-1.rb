def sum_it(nums)
  result = 0
  nums.each do |num|
    result += num
  end
  result
end

# brute is O(k*N)
def find_averages_of_subarrays_brute(k, nums)
  last_index = nums.length - k
  averages = []

  (0..last_index).each do |i|
    average = sum_it(nums.slice(i, k)) / k.to_f
    averages << average
  end

  averages
end

answer = find_averages_of_subarrays_brute(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print(answer == [2.2, 2.8, 2.4, 3.6, 2.8])

answer = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print(answer == [2.2, 2.8, 2.4, 3.6, 2.8])
