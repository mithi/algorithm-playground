=begin

puts Benchmark.measure {
  1_000_000.times do
    your_function
  end
}

0.810000   0.000000   0.810000 (  0.816964)

- user CPU time (the time spent executing your code),
- the system CPU time (the time spent in the kernel),
- both user and system CPU time added up,
- and the actual time (or wall clock time)
  it took for the block to execute in brackets.
=end

require 'benchmark'
require 'test/unit'
include Test::Unit::Assertions


def compare_to_order x, y, z
  if x > y

    if y > z
      return [x, y, z]
    end

    if x > z
      return [x, z, y]
    end

    return [z, x, y]

  elsif x > z
    return [y, x, z]
  elsif y > z
    return [y, z, x]
  end

  return [z, y, x]
end


def case_to_order x, y, z
  case
  when (x > y and y > z)
    return [x, y, z]
  when (x > z and z > y)
    return [x, z, y]
  when (y > x and x > z)
    return [y, x, z]
  when (y > z and z > x)
    return [y, z, x]
  when (z > x and x > y)
    return [z, x, y]
  end
  [z, y, x]
end


def minmax_to_order x, y, z
  min = [[x, y].min, z].min
  max = [[x, y].max, z].max
  mid = x + y + z - min - max
  [max, mid, min]
end


def swap_to_order x, y, z
  if y > x
    x, y = y, x
  end

  if z > x
    x, z = z, x
  end # x is now the largest

  if z > y
    y, z = z, y
  end

  [x, y, z]
end

# -----------------------
# Arguments
# -----------------------
N = 1_000_000
correct = 3, 2, 1

TEST_VALUES = [
  [1, 2, 3],
  [1, 3, 2],
  [2, 1, 3],
  [2, 3, 1],
  [3, 1, 2],
  [3, 2, 1],
]

# -----------------------
# Tests
# -----------------------
TEST_VALUES.each do |a, b, c|
  assert_equal correct, swap_to_order(a, b, c)
  assert_equal correct, compare_to_order(a, b, c)
  assert_equal correct, case_to_order(a, b, c)
  assert_equal correct, minmax_to_order(a, b, c)
end

puts "-----------------------"
puts "Benchmarks"
puts "-----------------------"
Benchmark.bm do |benchmark|
  benchmark.report("compare_to_order") do
    N.times do
      TEST_VALUES.each do |a, b, c|
        compare_to_order a, b, c
      end
    end
  end

  benchmark.report("swap_to_order") do
    N.times do
      TEST_VALUES.each do |a, b, c|
        swap_to_order a, b, c
      end
    end
  end

  benchmark.report("case_to_order") do
    N.times do
      TEST_VALUES.each do |a, b, c|
        case_to_order a, b, c
      end
    end
  end

  benchmark.report("minmax_to_order") do
    N.times do
      TEST_VALUES.each do |a, b, c|
        minmax_to_order a, b, c
      end
    end
  end
end


puts "-----------------------"
puts "Benchmarks = Refactored"
puts "-----------------------"
def run_benchmark benchmark, name, &block
  benchmark.report(name) do
    N.times do
      TEST_VALUES.each do |a, b, c|
        block.call(a, b, c)
      end
    end
  end
end

Benchmark.bm do |benchmark|

  run_benchmark(benchmark, "compare_to_order") do |a, b, c|
    compare_to_order(a, b, c)
  end

  run_benchmark(benchmark, "swap_to_order") do |a, b, c|
    swap_to_order(a, b, c)
  end

  run_benchmark(benchmark, "case_to_order") do |a, b, c|
    case_to_order(a, b, c)
  end

  run_benchmark(benchmark, "minmax_to_order") do |a, b, c|
    minmax_to_order(a, b, c)
  end
end

=begin

$ ruby benchmark-3sort.rb
-----------------------
Benchmarks
-----------------------
       user     system      total        real
compare_to_order  1.373110   0.003696   1.376806 (  1.382918)
swap_to_order  1.484355   0.004148   1.488503 (  1.493432)
case_to_order  1.778658   0.004350   1.783008 (  1.787654)
minmax_to_order  4.571116   0.011272   4.582388 (  4.595222)
-----------------------
Benchmarks = Refactored
-----------------------
       user     system      total        real
compare_to_order  1.956576   0.005035   1.961611 (  1.967270)
swap_to_order  2.077086   0.005206   2.082292 (  2.087581)
case_to_order  2.392941   0.005235   2.398176 (  2.405162)
minmax_to_order  5.140674   0.012765   5.153439 (  5.167528)

=end

