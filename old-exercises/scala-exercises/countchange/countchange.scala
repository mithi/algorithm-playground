/*************

 a recursive function that counts
 how many different ways you can make change for an amount given a list of coin denominations.
 For example, there are 3 ways to give change for 4 if you have coins with denomination 1 and 2:
 1+1+1+1, 1+1+2, 2+2.
 
 *************/


object session{
  
  def countChange(money: Int, coins: List[Int]): Int = {
  
    def count(m: Int, c: List[Int]): Int = {
      if (m == 0) 1
      else if (c.isEmpty || m < 0) 0
      else count(m - c.head, c) + count(m, c.tail)
    }
  
    if (money == 0) 0 else count(money, coins)
  }

  def main(args: Array[String]){
    println(countChange(4, Array(1, 2).toList))
    println(countChange(0, Array(1, 2).toList))
    println(countChange(4, Array().toList))

  }
}