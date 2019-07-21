# Greatest Common Factor
# ------------------------------------------------------------------------------
# Return the greatest number which is a factor of both inputs.
#
# The greatest common factor of 6 and 10 is 2
# the greatest common factor of 10 and 15 is 5

def greatest_common_factor(first_number, second_number)
  x, y = first_number, second_number
  n = x < y ? x : y
  n.downto(1).each do |i|
    if x % i == 0 and y % i == 0
      return i
    end
  end
  1
end

puts "-------Greatest Common Factor-------"

puts greatest_common_factor(6, 10) == 2
puts greatest_common_factor(10, 15) == 5
puts greatest_common_factor(4, 7) == 1
puts greatest_common_factor(4, 8) == 4

# Panoramic Pairs
# ------------------------------------------------------------------------------
# You have a panoramic view in front of you, but you only can take a picture of
# two landmarks at a time (your camera is small).  You want to capture every
# pair of landmarks that are next to each other.
#
# Given an array of landmarks, return every adjacent pair from left to right.
# Assume the panorama wraps around.

def panoramic_pairs(landmarks)
  n = landmarks.length - 1
  pairs = []

  (0...n).each do |i|
    pairs << [landmarks[i], landmarks[i + 1]]
  end

  pairs << [landmarks[-1], landmarks[0]]
  pairs
end

puts "-------Panoramic Pairs-------"

landmarks_1 = ["House", "Horse"]
pairs_1 = [["House", "Horse"], ["Horse", "House"]]

puts panoramic_pairs(landmarks_1) == pairs_1

landmarks_2 = ["Tree", "Mountain", "Ocean", "Cottage"]
pairs_2 = [["Tree", "Mountain"], ["Mountain", "Ocean"], ["Ocean", "Cottage"], ["Cottage", "Tree"]]

puts panoramic_pairs(landmarks_2) == pairs_2


# Two Degrees of Separation
# ------------------------------------------------------------------------------
# You have a hash that represents all of Facebook (lookit you).  Each key is the
# name of a person on facebook, and each value is an array of all their friends.
# Assume everyone on Facebook has a different name.
#
# Given Facebook and the name of a person, return an array of all the friends
# of their friends. Do not include the original person or their immediate friends.

def two_degrees_away(facebook, name)
  # facebook: key: name, value: array of friends
  # only friends of friends, NOT mutual friend

  my_friends = facebook[name]
  # I'm also "my friend"
  my_friends << name

  their_friends = []

  my_friends.each do |my_friend|
    her_friends = facebook[my_friend]
    her_friends.each do |her_friend|
      # if my friends, friend is not a mutual connection
      if !my_friends.include?(her_friend)
        their_friends << her_friend
      end
    end
  end
  their_friends
end


puts "-------Two Degrees of Separation-------"

facebook_1 = {
  "Harry Potter" => ["Ron Weasley"],
  "Ron Weasley" => ["Harry Potter", "Fred Weasley"],
  "Fred Weasley" => ["Ron Weasley"]
}

friends_1 = ["Fred Weasley"]

puts two_degrees_away(facebook_1, "Harry Potter") == friends_1


facebook_2 = {
  "Mark Zuckerberg" => ["Eduardo Saverin", "Dustin Moskovitz", "Sean Parker"],
  "Eduardo Saverin" => ["Mark Zuckerberg", "Tyler Winklevoss", "Cameron Winklevoss", "Dustin Moskovitz"],
  "Tyler Winklevoss" => ["Eduardo Saverin"],
  "Cameron Winklevoss" => ["Eduardo Saverin"],
  "Dustin Moskovitz" => ["Mark Zuckerberg", "Eduardo Saverin"],
  "Sean Parker" => ["Mark Zuckerberg"]
}

friends_2 = ["Tyler Winklevoss", "Cameron Winklevoss"]

puts two_degrees_away(facebook_2, "Mark Zuckerberg") == friends_2


# Assign Pods
# ------------------------------------------------------------------------------
# You are a JumpStart TA and you need to assign students to sit with other
# students who are at the same place in the curriculum.
#
# Given a list of students ordered by how far they are in the course and a
# list of pods, return their seat assignments.  Assume you can only seat four
# people per pod.  "Fill up" each pod as you go.  It's OK to have a pod with
# four people and the next pod with one person).  It's OK to have empty pods
# if there aren't enough students.

def assign_pods(students, pods)
  # four people per pod
  # if pod is empty will not be included in the
  # hashmap
  assignments = Hash.new([])
  j = nil
  pods.each_with_index do |pod, i|
    x, y = 4*i, 4*(i + 1)
    row = students[x...y]
    assignments[pod] = row
    if x >= students.length or y >=students.length
      break
    end
  end
  assignments
end

puts "-------Assign Pods-------"

students_1 = [
  "Scott",
  "Asher",
  "Julie",
  "Rick",
  "Jeff",
  "Brooke",
  "Sandra",
  "Jim",
  "Pete",
  "Marta",
  "Tanna"
]

pods_1 = [
  "Fremont",
  "Berkeley",
  "San Ramon"
]


expected_pod_assignment_1 = {
  "Fremont" => ["Scott", "Asher", "Julie", "Rick"],
  "Berkeley" => ["Jeff", "Brooke", "Sandra", "Jim"],
  "San Ramon" => ["Pete", "Marta", "Tanna"]
}

students_2 = [
  "Scott",
  "Asher",
  "Julie",
  "Rick",
  "Jeff",
  "Brooke",
  "Sandra",
  "Jim",
  "Pete",
  "Marta",
  "Tanna",
  "Fred",
  "George"
]

pods_2 = [
  "Fremont",
  "Berkeley",
  "San Ramon",
  "Oakland"
]


expected_pod_assignment_2 = {
  "Fremont" => ["Scott", "Asher", "Julie", "Rick"],
  "Berkeley" => ["Jeff", "Brooke", "Sandra", "Jim"],
  "San Ramon" => ["Pete", "Marta", "Tanna", "Fred"],
  "Oakland" => ["George"]
}

puts assign_pods(students_1, pods_1) == expected_pod_assignment_1
puts assign_pods(students_2, pods_2) == expected_pod_assignment_2


# Remove Letter 'A'
# ------------------------------------------------------------------------------
# Given a list of words, remove all the occurrences of the letter 'a' in those
# words.

def remove_letter_a(words)
  new_words = []
  words.each do |word|
    without_a = ""
    word.each_char do |c|
      if c != 'a'
        without_a << c
      end
    end
    new_words << without_a
  end
  new_words
end

puts "-------Remove Letter 'A'-------"

words_1 = ["blueberry", "apple", "banana", "peach"]
without_a_1 = ["blueberry", "pple", "bnn", "pech"]

words_2 = ["syllabus", "smirk", "salamander", "saaaaaaa"]
without_a_2 = ["syllbus", "smirk", "slmnder", "s"]

puts remove_letter_a(words_1) == without_a_1
puts remove_letter_a(words_2) == without_a_2
