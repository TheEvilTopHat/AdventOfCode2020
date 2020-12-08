import random

#program vars
program = []
program_copy = []
accumulator = 0
pointer = 0

#debug vars
breakpoints = []
lines_run = []
nop_jmp_lines = []

def get_code():
    global program
    global program_copy
    line_number = 0
    with open("input.txt", "r") as f:
        while True:
            line = f.readline()
            if line:
                line = line.strip()
                line = line.lstrip()
                program.append(line)
                if "nop" in line or "jmp" in line:
                    nop_jmp_lines.append(line_number)
                line_number += 1
            else:
                break
    program_copy = program.copy()


def go_to_next_line():
    global program
    global pointer
    pointer += 1
    return pointer < len(program)

def no_operation(sint):
    return go_to_next_line()

def accumulator_operation(sint):
    global accumulator
    accumulator += sint
    return go_to_next_line()

def jump_to(line):
    global program
    global pointer
    pointer += line
    return pointer < len(program)

def stop_code():
    print("POINTER",pointer)
    print("ACCUMULATOR",accumulator)
    if pointer < len(program):
        print("LINE",program[pointer])
    input("press a enter to continue")

def reset_program():
    global pointer
    global accumulator
    global lines_run
    global program
    global program_copy
    pointer = 0
    accumulator = 0
    lines_run = []
    program = program_copy.copy()

def change_random_line():
    choice = -1
    while True:
        choice = nop_jmp_lines.pop(0)
        line = program[choice]
        if "nop" in line or "jmp" in line:
            break
    line = program[choice]
    if "nop" in line:
        line = line.replace("nop","jmp")
    else:
        line = line.replace("jmp","nop")
    program[choice] = line
    
def run_code():
    operations = {
        "nop":no_operation,
        "acc":accumulator_operation,
        "jmp":jump_to 
    }

    while True:
        #read next line
        if pointer >= len(program):
            break
        line = program[pointer]
        if pointer in breakpoints or pointer in lines_run:
            #stop_code()
            reset_program()
            change_random_line()
            continue
        lines_run.append(pointer)
        #do operators
        op, sint = line.split(' ')
        if operations[op](int(sint)) != True: #keep running
            break
    print("PROGRAM FINISHED WITHOUT ERROS")
    stop_code()

if __name__ == "__main__":
    get_code()
    run_code()
