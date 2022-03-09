# Sokoban Tester
Functional tests for Sokoban

## How to use ?

- Copy your sokoban bin at the root of the repository
- Run ```
./tester.sh```

Don't touch your keyboard during the crawling :)

A **trace.txt** file will be outputed.

## Add your tests !

Create a new folder in **"tests/"** named as you want (without spaces).

In this folder create a **map.txt** file which will be the map for your Sokoban and a **test.txt** structured like this :
```
<expected return value>
<instructions>
...
```

### Example:

```
0
UP
LEFT
LEFT
DOWN
```
Instructions are `UP`, `LEFT`, `DOWN` and `RIGHT`.
