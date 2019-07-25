def sum_it(nums):
    result = 0
    for num in nums:
        result += num

    return result

# brute is O(k*N)
def find_averages_of_subarrays_brute(k, nums):

    averages = []
    end = len(nums) - k + 1

    for i in range(end):
        subarray = nums[i:(i + k)]
        average = sum(subarray) / k
        averages.append(average)

    return averages


answer = find_averages_of_subarrays_brute(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print(answer == [2.2, 2.8, 2.4, 3.6, 2.8])

answer = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
print(answer == [2.2, 2.8, 2.4, 3.6, 2.8])
