# Evalexpress Checker
Script to compare your evalexpress function to bash "bc" results on complex expressions

## Usage
- Place the script in the same directory as the bin of your evalexpr
- Use `python3 ./checker.py`
- The script will stop when your evalexpr don't match the expected output

## Known issues
- Sometimes intermediary operations reach int limit, your program may not handle it, so consider it while checking your program
