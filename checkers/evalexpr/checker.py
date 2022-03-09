from random import *
import subprocess
import sys
import warnings

warnings.filterwarnings("ignore")

nb_prob = 50
open_prob = 100
prob_end = 5
num_range = [0, 100]
expr = ""
operators = ["+","-","*","/", "%"]
opened_p = 0
min_expr_len = 5
max_expr_len = 30
no_overflow = False
error = False
def append_number():
    global expr
    if (len(expr) > 0 and expr[len(expr) - 1] in operators):
        expr += str(randint(num_range[0],num_range[1]))

def append_ope():
    global expr
    if (len(expr) > 0 and (expr[len(expr) - 1].isnumeric() or expr[len(expr) - 1] == ")")):
        expr += operators[randint(0,4)]
def str_to_stdout(s):
    ex = subprocess.Popen(['echo', s],stdout=subprocess.PIPE)
    return ex.stdout

while not error:
    while not no_overflow:
        while (len(expr) < min_expr_len or randint(0,100) > prob_end) and len(expr) < max_expr_len:
            if randint(0,100) < nb_prob:
                append_ope()
                expr += str(randint(num_range[0],num_range[1]))
                expr += operators[randint(0,4)]
                nb_prob = 50
                if (opened_p > 0):
                    open_prob = 25
                else:
                    open_prob = 100
            else:
                if (randint(0,100) < open_prob):
                    expr += "("
                    nb_prob = 100
                    opened_p += 1
                    if (opened_p > 0):
                        open_prob = 0
                    else:
                        open_prob = 100
                else:
                    append_number()
                    opened_p += -1
                    expr += ")"
                    if (opened_p > 0):
                        open_prob = 25
                    else:
                        open_prob = 100
        append_number()
        while expr[len(expr) - 1].isnumeric() == "(":
            expr = expr[:-1]
            opened_p+= -1
        while opened_p > 0:
            expr += ")"
            opened_p+= -1
        expr = expr.replace("()","1")
        try:
            ex = subprocess.Popen('bc',stdin=str_to_stdout(expr),stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            tmp_res, err = ex.communicate()
            tmp_res = int(tmp_res.decode('ascii').replace("\n",""))
            no_overflow = True
            if tmp_res > 1000000 or tmp_res < -1000000:
                raise Exception()
        except:
            expr = ""
            open_prob = 100
            nb_prob = 50
            no_overflow = False
    ex = subprocess.Popen(['./eval_expr',expr],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    result, err = ex.communicate()
    ex = subprocess.Popen('bc',stdin=str_to_stdout(expr),stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    solution, err = ex.communicate()
    solution = int(solution.decode('ascii').replace("\n",""))
    print("With expr : \"" +expr + "\"\nGot : " + result.decode('ascii').replace("\n","") + "\nExpected : "+ str(solution))
    if int(result) != solution:
        print("ERROR\n\n")
        error = True
    else:
        print("PASS\n\n")
    expr = ""
    open_prob = 100
    nb_prob = 50
    no_overflow = False
