#!/usr/bin/python3

import sys

def is_in_order(list: list):
    for i in range(0, len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

def swap_firsts(list: list):
    tmp = list[0]
    list[0] = list[1]
    list[1] = tmp
    return list

def rotate(list: list):
    list.append(list.pop(0))
    return list


def reverse_rotate(list: list):
    list.insert(0, list.pop())
    return list


def push(list_a: list, list_b: list):
    list_b.insert(0, list_a.pop(0))
    return [list_a, list_b]


def execute_instruction(instructions, number_list):
    list_b = []
    print(f"Executing {len(instructions.split())} instructions on The List")
    for instruction in instructions.split(' '):
        if instruction == 'ra':
            number_list = rotate(number_list)
        elif instruction == 'rra':
            number_list = reverse_rotate(number_list)
        elif instruction == 'pb':
            r = push(number_list, list_b)
            number_list = r[0]
            list_b = r[1]
        elif instruction == 'pa':
            r = push(list_b, number_list)
            number_list = r[1]
            list_b = r[0]
        elif instruction == 'sa':
            number_list = swap_firsts(number_list)
        elif instruction == 'sb':
            list_b = swap_firsts(list_b)
        elif instruction == 'sc':
            number_list = swap_firsts(number_list)
            list_b = swap_firsts(list_b)
        elif instruction == 'rr':
            number_list = rotate(number_list)
            list_b = rotate(list_b)
        elif instruction == 'rrr':
            number_list = reverse_rotate(number_list)
            list_b = reverse_rotate(list_b)
        else:
            print("Invalid instruction")
            sys.exit(1)
    if (len(list_b) != 0):
        print("Error: list b not empty")
        # Print a colored KO
        print("\033[91mKO\033[0m")
        sys.exit(1)
    if (is_in_order(number_list)):
        print("The List is in order")
        print("\033[92mOK\033[0m")
        sys.exit(0)
    else:
        print("The List is not in order")
        print("\033[91mKO\033[0m")
        sys.exit(1)


def file_to_int_list(file_name):
    list = []
    with open(file_name, 'r') as f:
        for num in f.read().split():
            list.append(int(num))
    return list


def file_to_string(file_name):
    with open(file_name, 'r') as f:
        return f.read().strip()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(
            "Usage: ./push_swap.py [list of numbers - file] [list of instructions - file]")
        exit(1)
    number_list = file_to_int_list(sys.argv[1])
    instructions = file_to_string(sys.argv[2])
    execute_instruction(instructions, number_list)
