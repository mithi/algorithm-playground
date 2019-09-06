# Swap function
tldr do this
```ruby
x, y = 3, 4
y, x = x, y
```
this below is impossible to achieve in Ruby
- There is no way to get access to the name of the arguments outside a function, so we can't rebind them.
```ruby
x, y = 3, 4
swap(x, y)
# Now x = 4, y = 3
```

in C this is possible
```c
void swap (int* xp, int* yp) {
  int z = *yp;
  *yp = *xp;
  *xp = z;
}

void main () {
  int x = 3;
  int y = 4;

  swap(&x, &y);
  // Now x == 4 and y == 3.
}
```
- `&x` returns a pointer, which is the memory address which the value for x lives in
- The swap function takes in two pointers (that's what `int*` means); it does not take two int values.
- `*yp` means to pull the value out of the memory address yp and stores this in memory for the variable z.
-  Pull out the value at memory address `xp` (`*xp`) and copy it into memory address `yp` (`*yp = ...`).
- Lastly, we copy the value of z (previous memory of `*yp` before assignment) into memory address xp.
