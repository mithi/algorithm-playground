/*******

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1

 *******/
object session {
  
  def pascal(c: Int, r: Int): Int = {
    if (c == 0 || c == r) 1 else pascal(c - 1, r - 1) + pascal(c, r - 1)
  } 

  def printPascal(r: Int) = {
    for (row <- 0 to r){
      for (col <- 0 to row)
        print( pascal(col, row) + " ")
      println()
    }
  }

  def main(args: Array[String]) {
    printPascal(20)
  }
}