# PUSHSWAP UTILS

## Number generator
Usage :
```
python3 gen_nb.py <number count> <min val> <max val>
```

It will output your number list in stdout. You can redirect it to a file :
```
python3 gen_nb.py ... > numbers.txt
```

## Pushswap tester
Usage :
First, run your pushswap with a list of numbers stored in a file and redirect output to a file:
```
./push_swap $(< numbers.txt) > instructions.txt
```

Then run the tester with the two lists :
```
python3 tester.py numbers.txt instructions.txt
```

It will print "Pushswap OK" if your pushswap worked or "Pushswap KO" otherwise.
