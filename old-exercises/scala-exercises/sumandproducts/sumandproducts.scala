object session{

  def sum(f: Int => Int): (Int, Int) => Int = {
    
    def sumF(a: Int, b: Int): Int = {  
      def loop(x: Int, acc: Int): Int = 
        if(x > b) acc else loop(x + 1,  f(x) + acc)
      
      loop(a, 0)
    }
    sumF
  }

  def product(f: Int => Int): (Int, Int) => Int = {
    
    def productF(a: Int, b: Int): Int = {
      def loop(x: Int, acc: Int): Int = 
        if(x > b) acc else loop(x + 1,  f(x)*acc)
        
      loop(a, 1)
    }
    productF
  }

  def fact(a: Int): Int = 
    product(x => x)(1, a)

  def main(args: Array[String]): Unit = {

    print("summation from 1 to 5 inclusive: ")
    println(sum(x => x)(1, 5))

    print("summation of cubes from 2 to 4 inclusive: ")
    println(sum(x => x*x*x)(2, 4))

    print("product from 1 to 5 inclusive: ")
    println(product(x => x)(1, 5))

    print("product of cubes from 2 to 4 inclusive: ")
    println(product(x => x*x*x)(2, 4))

    print("factorial of 5: ")
    println(fact(5))

    print("summation of factorials from 4 to 6 inclusive: ")
    println(sum(fact)(4, 5))
  }
}