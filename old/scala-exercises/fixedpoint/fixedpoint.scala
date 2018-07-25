/***********************
 *
 * x is a fixed point of a function if: f(x) = x
 * 1 = x / f(x)
 * estimate fix point: 
 * start with initial estimate then
 * apply f in a repetitve way... 
 * x, f(x), f(f(x)), f(f(f(x))), ...
 * until value does not vary that much anymore
 *
 * sqrt(a) = b, b*b = a , b = b/a
 * x is a fixed point of f(x) = x
 * b is a fixed point of f(b) = b/a = b 
 *
 ***********************/

 // def sqrt (x: Double) = fixedPoint(y => x / y)(1.0) 
 // srqrt(2) does not converge because it oscillations too much = 2, 1, 2, 1
 // control oscillation by preventing estimates from varying too much - successive approximation

 
object session {

  def abs(x: Double) = if(x < 0) -x else x
  
  val tolerance = 0.0001
  def isCloseEnough(x: Double, y: Double) = 
    abs((x - y) / x) < tolerance

  def fixedPoint (f: Double => Double)(firstGuess: Double) = {  

    def iterate(guess: Double): Double = {
      val next = f(guess)
      if(isCloseEnough(guess, next)) next else iterate(next)
    }
      
    iterate(firstGuess)
  }  
  
  def averageDamp(f: Double => Double)(x: Double) = 
    (x + f(x)) / 2

  def sqrt(x: Double) = 
    fixedPoint(averageDamp(y => x / y))(1.0)

  def main(args: Array[String]): Unit = {
    println(sqrt(2.0))
  }
}