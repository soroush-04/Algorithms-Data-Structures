"""Let’s print a triangle made of asterisks (‘*’) separated by spaces and consisting
of n rows again, but this time upside down, and make it symmetrical. Consecutive rows should
contain 2n − 1, 2n − 3, . . . , 3, 1 asterisks and should be indented by 0, 2, 4, . . . , 2(n − 1)
spaces. For example, for n = 4 the triangle should appear as follows:
* * * * * * *
  * * * * *
    * * *
      * 
"""


def triangle(n):
    for i in range(n, 0, -1):
        print(" " * (2 * (n - i)), end="")
        print("* " * (2 * i - 1))


triangle(4)
