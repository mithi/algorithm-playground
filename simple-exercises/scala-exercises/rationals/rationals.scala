
class Rational(x: Int, y: Int) {
  
  private def gcd(a: Int, b: Int): Int = if (b == 0) a else gcd(b, a % b) 
  private val g = gcd(x, y)
  val n = x / g
  val d = y / g
  
  def inverse: Rational = new Rational (this.d,  this.n)

  def neg: Rational = new Rational(-this.n, this.d)

  // a/b + x/y = (ay + bx) / by
  def add(that: Rational) = new Rational (this.n * that.d + this.d * that.n, this.d * that.d) 
  
  def mul(that: Rational) = new Rational (this.n * that.n, this.d * that.d)

  def sub(that: Rational) = add(that.neg)

  def div(that: Rational) = mul(that.inverse)

  override def toString = this.n + "/" + this.d

}

object session{
  
  def main (args: Array[String]): Unit = {
    val x = new Rational(1, 3)
    val y = new Rational(5, 7)
    val z = new Rational(3, 2)
    println(x.sub(y).sub(z))      // x - y - z = 79 / 42
    println(x.add(y).mul(z))      // (x + y) * 2 = 11 / 7
  }
}