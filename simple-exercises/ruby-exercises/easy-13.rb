# @param {String} s
# @return {Boolean}
def is_valid(s)
  openstack = []
  open_pairs = {
    "(" => ")",
    "{" => "}",
    "[" => "]", 
  }
  
  # this can be a set
  close_pairs = {
    ")" => "(",
    "}" => "{",
    "]" => "[",
  }

  s.each_char do |ch|
    if open_pairs.include?(ch)
      openstack << ch
    elsif close_pairs.include?(ch)
      return false if openstack.empty?
      symbol = openstack.pop
      return false if open_pairs[symbol] != ch
    end
  end
    
  openstack.empty? ? true : false
end

# Algorithm 
# iterate thru each char
# if we encounter an open symbol 
#  -> add to stack
#  -> then move to next char
# if we encounter a close symbol 
#  -> there's no open symbol in the stack 
#     then this is invalid
#  -> if the most recent open symbol in the stack 
#      is not the same as the close symbol
#      then this is invalid
#  -> if they're pairs remove the open symbol 
#       since we already found its pair
# if we have seen all characters 
#   and there's still an open symbol without a pair
#   then this is invalid
# else this is valid

=begin
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true

Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false

Example 4:

Input: "([)]"
Output: false

Example 5:

Input: "{[]}"
Output: true

An interesting property about a valid parenthesis expression is that a sub-expression of a valid expression should also be a valid expression. (Not every sub-expression) e.g.

{ { } [ ] [ [ [ ] ] ] } is VALID expression
          [ [ [ ] ] ]    is VALID sub-expression
  { } [ ]                is VALID sub-expression

What if whenever we encounter a matching pair of parenthesis in the expression, we simply remove it from the expression? This would keep on shortening the expression. e.g.

{ { ( { } ) } }
      |_|

{ { (      ) } }
    |______|

The stack data structure can come in handy here in representing this recursive structure of the problem. We can't really process this from the inside out because we don't have an idea about the overall structure. But, the stack can help us process this recursively i.e. from outside to inwards.

=end
