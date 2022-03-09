#This one will work :hope:

import sys

file_opened = open("./"+sys.argv[1], 'r')
stack_a = file_opened.read().replace('\n', '').replace('\0', '').split(' ')
file_opened = open("./"+sys.argv[2], 'r')
operations = file_opened.read().replace('\n', '').replace('\0', '').split(' ')
len_a = len(stack_a)
stack_b = []

if len_a == 1:
    print("\033[92mPushswap OK\033[0m")

def is_sorted():
    global stack_a, len_a
    if len(stack_a) != len_a:
        return (False)
    for i in range(1, len_a):
        if int(stack_a[i]) < int(stack_a[i - 1]):
            return (False)
    return (True)

def sa():
    global stack_a
    if len(stack_a) >= 2:
        stack_a[0], stack_a[1] = stack_a[1], stack_a[0]
def sb():
    global stack_b
    if len(stack_b) >= 2:
        stack_b[0], stack_b[1] = stack_b[1], stack_b[0]
def pa():
    global stack_a, stack_b
    if len(stack_b) > 0:
        stack_a.insert(0, stack_b.pop(0))
def pb():
    global stack_a, stack_b
    if len(stack_a) > 0:
        stack_b.insert(0, stack_a.pop(0))
def ra():
    global stack_a
    if len(stack_a) > 0:
        stack_a.append(stack_a.pop(0))
def rb():
    global stack_b
    if len(stack_b) > 0:
        stack_b.append(stack_b.pop(0))
def rra():
    global stack_a
    if len(stack_a) > 0:
        stack_a.insert(0, stack_a.pop(len(stack_a) - 1))
def rrb():
    global stack_b
    if len(stack_b) > 0:
        stack_b.insert(0, stack_b.pop(len(stack_b) - 1))

for i in range(len(operations)):
    if operations[i] == "sa":
        sa()
    if operations[i] == "sb":
        sb()
    if operations[i] == "pa":
        pa()
    if operations[i] == "pb":
        pb()
    if operations[i] == "ra":
        ra()
    if operations[i] == "rb":
        rb()
    if operations[i] == "rra":
        rra()
    if operations[i] == "rrb":
        rrb()

if is_sorted():
    print("\033[92mPushswap OK\033[0m")
else:
    print("\033[91mPushswap KO\033[0m")
