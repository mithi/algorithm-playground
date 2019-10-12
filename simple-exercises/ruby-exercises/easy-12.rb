def build_say(string)
  result = ""
  ch = string[0]
  count = 0
    
  string.each_char do |current|
    if current == ch
      count += 1
    else
      result << "#{count}#{ch}"
      ch = current
      count = 1
    end
  end
  result << "#{count}#{ch}"
  result
end

def count_and_say(n)
  "1" if n == 1

  (n - 1).times.inject("1") do |result, _|
    build_say(result)
  end
end
