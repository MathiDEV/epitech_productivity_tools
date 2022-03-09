##
## EPITECH PROJECT, 2021
## B-CPE-101-LYN-1-1-bistromatic-joshua.brionne
## File description:
## deBugIstro.py
##

from random import *
import subprocess
import string

# Classes

class Expression:
    pass

class Number(Expression):
    def __init__(self, num):
        self.num = num

    def __str__(self):
        return str(self.num)

class BinaryExpression(Expression):
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return str(self.left) + self.op + str(self.right)

class ParenthesizedExpression(Expression):
    def __init__(self, exp):
        self.exp = exp

    def __str__(self):
        return "(" + str(self.exp) + ")"

# Random expr

def random_num():
    res = ""
    for i in range(0, randint(1, 4)):
        res += str(randint(0, 9))
    return res

def randomExpression(prob):
    p = random()
    if p > prob:
        return "#"
    elif randint(0, 1) == 0:
        return ParenthesizedExpression(randomExpression(prob / 1.2))
    else:
        left = randomExpression(prob / 1.2)
        op = choice(['+','-','*','/'])
        right = randomExpression(prob / 1.2)
        return BinaryExpression(left, op, right)

# Main functions

def random_base():
    if (randint(0, 3) < 3):
        base_chars = string.digits + string.ascii_uppercase
        return base_chars[0:randint(2,35)]
    else:
        base_chars = string.digits + string.ascii_uppercase + "+-*/,."
        res = ""
        i = 0
        while i < randint(2,15):
            rand_char = base_chars[randint(0, len(base_chars) - 1)]
            if not rand_char in res and rand_char != '%':
                res += rand_char
                i += 1
        return res

def random_operators(base):
    operators = string.ascii_letters + "+-*/,."
    res = ""
    i = 0
    while i < 6:
        rand_char = operators[randint(0, len(operators) - 1)]
        if not rand_char in res and not rand_char in base and rand_char != '#':
            res += rand_char
            i += 1
    return res

def convert(num, base):
    converted = ""
    while num > 0:
        converted += base[num % len(base)]
        num //= len(base)

    if len(converted) == 0:
        return "0"
    return converted[::-1]

def str_to_stdout(s):
    ex = subprocess.Popen(['echo', s],stdout=subprocess.PIPE)
    return ex.stdout

# Main loop

error = False

while not error:
    base = random_base()
    # random_operators(base) + 
    operators = "()+-*/%"
    true_calc = str(randomExpression(1))
    bistro_calc = true_calc
    bistro_calc = bistro_calc.replace('(', operators[0]).replace(')', operators[1]).replace('+', operators[2]).replace('-', operators[3]).replace('*', operators[4]).replace('/', operators[5])
    while ('#' in true_calc):
        number = random_num()
        true_calc = true_calc.replace('#', number, 1)
        bistro_calc = bistro_calc.replace('#', convert(int(number), base), 1)

    bistro = subprocess.Popen(['./calc', base, operators, str(len(bistro_calc))],stdin=str_to_stdout(bistro_calc), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, err = bistro.communicate()
    result = result.decode('ascii').replace("\n","")

    bc = subprocess.Popen('bc',stdin=str_to_stdout(true_calc), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    solution, err = bc.communicate()
    solution = convert(int(solution.decode('ascii').replace("\n","").replace("\\", "")), base)

    print("Command :")
    print("echo \""+bistro_calc+"\" | ./calc \""+base+"\" \""+operators+"\" "+str(len(bistro_calc)))
    print("Expected: "+solution)
    print("Got: "+result)
    if (result == solution):
        print("PASS\n\n")
    else:
        print("True expr: " + true_calc)
        print("ERROR\n\n")
        error = True

