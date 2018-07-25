object session {
  
  def factorial(n: Int): Int = {
    
    def loop( acc: Int, n: Int): Int = 
      if(n == 0) acc else loop(acc * n, n-1)
    
    loop(1, n)
  }
  
  /* Euclid's Algorithm - Greatest Common Denomination */
  def gcd(a: Int, b: Int): Int = 
    if (b == 0) a else gcd(b, a % b) 

  def main(args: Array[String]): Unit = {
    println(factorial(4))
    println(gcd(14, 21))
  }
}

/***********
 
 gcd - if (b == 0) a else gcd(b, a % b) 
 gcd (14, 21)
 if ( 21 == 0 ) 14 else gcd ( 21, 14 % 21)
 gcd ( 21 , 14 )
 if (14 == 0 ) 21 else  gcd ( 14, 21 % 14 )
 gcd ( 14, 7)
 if ( 7 == 0 ) 14 else gcd ( 7 , 7 % 14)
 gcd (7, 7)
 if ( 7 == 0 ) 7 else gcd ( 7, 7 % 7)
 gcd (7, 0) 
 if ( 0 == 0) 7 else gcd ( 0, 7 % 0 ) 
 7

 factorial - if (b == 0) a else gcd(b, a % b) 
 if (4 == 0) 1 else loop( 4*1, 3)
 loop(4, 3)
 if (3 == 0) 4 else loop( 3*4, 2)
 loop (12, 2)
 if (2 == 0) 12 else loop( 2*12, 1)
 loop(24, 1)
 if (1 == 0) 1 else loop (1*24, 0)
 loop(24, 0)
 if (0 == 0) 24 else loop( 0*24, 0)
 24 

**************/


