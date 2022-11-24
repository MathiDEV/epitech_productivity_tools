# PUSHSWAP UTILS

## Number generator
Usage :
```
Generator [number count] [min val] [max val]
```

It will output your number list in numbers.txt.
You can call the generator without any values.

## Pushswap tester
Usage :
First, run your pushswap with a list of numbers stored in a file and redirect output to a file:
```
./push_swap $(< numbers.txt) > instructions.txt
```

Then run the tester with the two lists :
```
tester numbers.txt instructions.txt
```

It will print "Pushswap OK" if your pushswap worked or "Pushswap KO" otherwise.

You can also use: 
- auto [number list size]:
  - Will generate a new list, launch your program and save instructions, and test it (timed)  
  - Parameter will change the lenght of the test list
- serial [difficulty]:
  - Will do multiple test with 5 numbers - [5, 10, 25, 50, 100]
  - Parameter will add a multiplier for difficulty (up to 10)
