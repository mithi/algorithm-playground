
class Rational(x: Int, y: Int) {

  require( y != 0, "denominator must be non-zero")
  def this(x: Int) = this(x, 1)
  
  private def abs(x: Int) = if (x > 0) x else -x
  private def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b) 
  private val g = gcd(abs(x), abs(y)) 
  
  val (n, d) = if (y < 0) (-x, -y) else (x, y)

  /***
   + + =>  x  y =>  1 /  2 =>  1 / 2   
   - - => -x -y => -1 / -2 =>  1 / 2
   + - => -x -y =>  1 / -2 => -1 / 2
   - + =>  x  y => -1 /  2 => -1 / 2
   ***/
  
  def inv : Rational = new Rational(this.d,  this.n)

  def neg : Rational = new Rational(-this.n, this.d)
  
  // a/b + x/y = (ay + bx) / by
  def + (that: Rational) = new Rational(this.n * that.d + this.d * that.n, this.d * that.d) 
  
  def * (that: Rational) = new Rational(this.n * that.n, this.d * that.d)

  def - (that: Rational) = this + that.neg

  def / (that: Rational) = this * that.inv
  
  // a/b < x/y iff ay < xb
  def < (that: Rational) =  this.n * that.d < that.n * this.d

  def > (that: Rational) =  this.n * that.d > that.n * this.d
  
  def == (that: Rational) = this.n * that.d == that.n * this.d 

  override def toString = if (this.d == 1 || this.n == 0) (this.n).toString else this.n + "/" + this.d
  
}

object session{
  
  def main (args: Array[String]): Unit = {
    
    val x = new Rational(1, 3)
    val y = new Rational(5, 7)
    val z = new Rational(3, 2)
    val m = new Rational(1, 2)
    val one = new Rational(1)
    val zero = new Rational(0)

    println(x * y)             // 1/3 * 5/7 = 5/ 21
    println((x * x) + (m * m)) // 13/36
    println(x - y)             // 1/3 - 5/7 = -8/21
    println(x > m)             // 1/3 > 1/2 false
    println(x < m)             // 1/3 < 1/2 true
    println(x == x)            // true
    println( x / m)            // (1/3)/(1/2) = 2/3
    println(one)
    println(zero)
  }
}