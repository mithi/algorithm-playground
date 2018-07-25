object session{
  
  def isBalanced1(chars: List[Char]): Boolean = {
    
    def next(chars: List[Char], counter: Int): Int = {
      if (chars.isEmpty) counter 
      else {
        if (chars.head == '(') next(chars.tail, counter + 1)
        else if (chars.head == ')'){ 
          if (counter == 0) -1
          else next(chars.tail, counter - 1)
        } else next(chars.tail, counter)
      }
    }

    if (next(chars, 0) == 0) true else false 
  }

  def isBalanced2(chars: List[Char]): Boolean = {

    def count(c: List[Char], counter: Int): Int = {
      if (c.isEmpty) counter 
      else {
        c.head match {
          case '(' => count(c.tail, counter + 1)
          case ')' => if (counter == 0) -1 else count(c.tail, counter - 1)
          case _   => count(c.tail, counter) 
        }
      }
    }

    if (count(chars, 0) == 0) true else false 
  }

  def main(args: Array[String]): Unit = {
    
    println("isBalanced1")
    println(isBalanced1("(just an) example".toList))
    println(isBalanced1("(if (zero? x) max (/ 1 x))".toList))
    println(isBalanced1("I told him (that it’s not (yet) done). (But he wasn’t listening)".toList))
    println(isBalanced1(":-)".toList))
    println(isBalanced1("())(".toList))

    println("isBalanced2")
    println(isBalanced2("(just an) example".toList))
    println(isBalanced2("(if (zero? x) max (/ 1 x))".toList))
    println(isBalanced2("I told him (that it’s not (yet) done). (But he wasn’t listening)".toList))
    println(isBalanced2(":-)".toList))
    println(isBalanced2("())(".toList))
  }
}
