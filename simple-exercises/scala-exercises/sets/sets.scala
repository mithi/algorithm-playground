object session {

  type Set = Int => Boolean

  def contains(s: Set, elem: Int): Boolean = s(elem)

  def singletonSet(elem: Int): Set =  x => x == elem

  def union(s: Set, t: Set): Set = x => s(x) || t(x)

  def intersect(s: Set, t: Set): Set = x => s(x) && t(x)

  // elements in set S that is not in set t 
  // ie (1, 2, 3) - (3, 4, 5) = (2, 3)
  def diff(s: Set, t: Set): Set = x => s(x) && !t(x)

  def filter(s: Set, p: Int => Boolean): Set = intersect(s, p)

  val bound = 50
  // if for all x in -1000 < x < 1000 that is in s satisfies p (ie in set p) then true, else false
  // if there is an x that is in the set of elements that is in s but not in p, then false 
  def forall(s: Set, p: Int => Boolean): Boolean = {
    def iter(x: Int): Boolean = {
      if (x > bound) true
      else if (contains(diff(s, p), x)) false
      else iter(x + 1)
    }
    iter(-bound)
  }

  // if there is one element of s that is in p then true (between -bound and bound)
  // if there is no element of s that is in p, then all elements of s is in !p, where everything - p = !p
  // if there is an element of s that is in p, then it is not true that all elements of s is in !p
  def exists(s: Set, p: Int => Boolean): Boolean = !forall(s, x => !p(x))
  
  // e.g. cube(x) = x*x*x then map({1,2,3}, cube) is {1, 8, 27} 
  // search for x that satisfies condition (between -bound and bound) because there no way to inverse an arbitrary f
  def map(s: Set, f: Int => Int): Set = x => exists(s, (y => f(y) == x))

  def setOfThree(a: Int, b: Int, c: Int): Set = x => x == a || x == b || x == c

  def multipleOf(n: Int): Set = x => (x % n == 0) && (x != 0) 

  def negInt: Set = x => x < 0

  def posInt: Set = x => x > 0

  def multipleOfBoth(a: Int, b: Int): Set = intersect(multipleOf(a), multipleOf(b))

  def multipleOfEither(a: Int, b: Int): Set = union(multipleOf(a), multipleOf(b))
  
  def toString(s: Set): String = {
    val xs = for (i <- -bound to bound if contains(s, i)) yield i
    xs.mkString("{", ",", "}")
  }

  def printSet(s: Set) {
    println(toString(s))  }

  def main(args: Array[String]): Unit = {
    
    println("negative integers")
    printSet(negInt)
    println("positive integers")
    printSet(posInt)
    println("multiples of 7")
    printSet(multipleOf(7))
    println("multiples of 4 and 6")
    printSet(multipleOfBoth(4, 6))
    println("multiples of 4 or 6")
    printSet(multipleOfEither(4, 6))

    val exampleSet: Set = setOfThree(7, 13, 17)
    val double: Set = map(setOfThree(7, 13, 17), x => 2*x)
    
    printSet(double)
    print("all elements of {7, 13, 17} are positive integers: ")
    println(forall(exampleSet, posInt)) //true

    print("all non-zero multiples of 6 are also non-zero multiples of 3 between -50 and 50: ")
    println(forall(multipleOf(6), multipleOf(3))) //true
    print("all non-zero multiples of 6 are also non-zero multiples of 4 between -50 and 50: ")
    println(forall(multipleOf(6), multipleOf(4))) //false

    print("there exists a non-zero multiple of 6 that is also a non-zero multiple of 13 between -50 and 50: ")
    println(exists(multipleOf(6), multipleOf(13))) //false
    printSet(intersect(multipleOf(6), multipleOf(13)))
    print("there exists a non-zero multiple of 6 that is also a non-zero multiple of 8 between -50 and 50: ")
    println(exists(multipleOf(6), multipleOf(8))) //true

  }
}
