# Recursion

Recursion is a way of running an action repeatedly without using loops. It is not used directly very
often in practice, but it is important to know.

In python (or most programming languages), there is nothing stopping you from calling a function
from within the same function.

For example:
```
def run_forever():
    print("Still running...")
    run_forever()
```

In this function, we print a message and then make a "recursive call" to the same function. This
function is not very useful, because it will just keep running forever, but it's possible to use
recursion in a sensible way by having a "base case".

## Base Case and Recursive Case

In a recursive function, there is usually an if-statement. One branch of the if-statement will
contain the base case, the other will contain the recursive case.

For example:
```
def recursive_fn(x):
    if x > 5:
        # This is the base case, because we don't call the function again
        print("Done!")
    else:
        # This is the recursive case, because we call the function again
        print(f"Counting {x}")
        recursive_fn(x + 1)
```

## Exercise

Create a function `sum_up_to(n)`, which takes a positive number n and returns the sum of the numbers
from 1 to n, but do not use any loops.

## Examples

```
sum_up_to(2) => 3
sum_up_to(3) => 6
sum_up_to(4) => 10
sum_up_to(10) => 55
```
