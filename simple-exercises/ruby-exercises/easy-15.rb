# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} l1
# @param {ListNode} l2
# @return {ListNode}
def merge_two_lists(l1, l2)
  return l2 if l1.nil? 
  return l1 if l2.nil?
  head1, head2 = l1, l2
  
  if l1.val > l2.val
    head1, head2 = l2, l1
  end
    
  bighead = head1

  loop do 
    while !head1.next.nil? and head1.next.val <= head2.val
      head1 = head1.next
    end
    
    pointer = head1.next
    head1.next = head2
    head1 = head2
    head2 = pointer
    break if head2 == nil
  end
  bighead
end

=begin
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
=end
