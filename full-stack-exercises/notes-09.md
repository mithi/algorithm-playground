# Additional Exercises


1.Monkey-patch these methods
```
# Enumerables
each
select
reject
any
all

# Array
zip
rotate
join
reverse
```
2. The Roadtrip Game `ghost`
3. A Maze Solver (shortest-path A-star)
```
****************
*         *   E*
*    *    *  ***
*    *    *    *
*    *    *    *
*    *    *    *
*S   *         *
****************
```
4. Eight Queens Puzzle
5. Project Euler - https://projecteuler.net/archives

# Notes
- Remember how pointers, references, assignments work
- The `=` operator does not mutate (modify) an object; it merely reassigns the variable so that it now refers to a new object
- Integer objects are immutable
```ruby
cats3 = Hash.new { |h, k| h[k] = [] }
```
```ruby
arr_of_arrs = Array.new(3) { [] }
```
```ruby
  x = 15
  def foo(x)
    x = 10
  end
  foo(x)
  p x # 15
```
```ruby
 x = []
  def foo(x)
    x << "Fancy Feast"
  end
  foo(x)
  p x # ["Fancy Feast"]
```

## Code Smells
- Callers do not typically expect you to modify an argument
- https://asherkingabramson.com/blog/productivity/learn-to-debug
- http://confreaks.tv/videos/aloharuby2012-refactoring-from-good-to-great
- **Duplicated/similar code**
- **Long methods**
- **Too many parameters**: The more parameters a method has, the greater the chance that it is too coupled to code that invokes it. Many parameters may also be a sign of an excessively complex method.
- **Data clump**: if you see a group of data always being passed around together, this is usually a good candidate for refactoring out into an object.
- **Long method chains**: long method chains can often be a sign that you're violating the Law of Demeter: only talk to your "neighbors", only use one dot.
- **Law of Demeter (LoD)**: Each unit should have only limited knowledge about other units: only units "closely" related to the current unit. Each unit should only talk to its friends; don't talk to strangers Only talk to your immediate friends. LoD has disadvantages (see the wiki article); if taken too literally you end up with overly wide interfaces. However, the longer your method chains get, the more likely you should apply LoD.
- **Indecent Exposure**: Classes should share the bare minimum interface with the outside world. If you don't have a compelling reason to make a method or variable public, hide it.
- **Speculative Generality**: Follow the principle of YAGNI ('You ain't gonna need it')
- **Dead code**: don't leave commented-out (or otherwise unused) code in your code base.
- **God object**: A god object is one that is very tightly connected to all the other objects in the system. Good OO design results in classes that are lightly coupled. A good class delegates responsibility as necessary to other objects; it shouldn't need to know everything about what every other object is doing (omniscience), and it shouldn't micromanage how other objects manage their responsibilities. Nothing in your program usually needs to even know about the existence of everything else.
```
game.board[pos].revealed = true if !guess && game.board[pos] && game.board[pos].revealed == false

Long method chain suggests Law of Demeter violation

We are chaining too many methods. The !if should be changed to unless when possible. We are relying on the board information on the game for every call instead of being able to call a method directly on the game. And the game.board[pos] is repeated many times making it complicated to understand right off the bat.
```
