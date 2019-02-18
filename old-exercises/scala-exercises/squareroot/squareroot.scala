object session {

/*
 * Square Root with Newton's Method (successive approximation)
 * - Start with an initial estimate (y = 1)
 * - Repeatedly improve the estimate by taking the mean of y and x/y
 * 
 */

  def abs(x: Double) = if(x < 0) -x else x 

  def sqrt(x: Double) = {
      
    def sqrtIter(guess: Double): Double =
      if (isGoodEnough(guess)) guess else sqrtIter(improve(guess))
    
    def isGoodEnough(guess: Double) = 
      abs(guess * guess - x) / x < 0.001

    def improve(guess: Double) = 
      (guess + x / guess) / 2
  
    sqrtIter(1.0)
  }

  def main(args: Array[String]): Unit = {
    println("hello world!");
    println(sqrt(1))
    println(sqrt(2))
    println(sqrt(4))
    println(sqrt(1e-6))
    println(sqrt(1e60))
  }
}