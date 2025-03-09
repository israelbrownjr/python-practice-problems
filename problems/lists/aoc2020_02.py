"""
Starter code for Advent of Code 2020 Day #2

You must implement functions part1 and part2
"""

import sys
import os


def part1(passwords):
    """
    Solves Part 1 (see problem statement for more details)

    Parameter:
    - passwords (list of strings)

    Returns an integer
    """
    quant_valid = 0
    for line in passwords:
        quant_char = 0
        line = line.split()
        #Bounds
        bounds = line[0].split('-')
        lower_bound = int(bounds[0])
        upper_bound = int(bounds[1])
        target = line[1][0]
        for char in line[2]:
            if char == target:
                quant_char += 1
        if lower_bound <= quant_char and quant_char <= upper_bound:
            quant_valid += 1
    return quant_valid



def part2(passwords):
    """
    Solves Part 2 (see problem statement for more details)

    Parameter:
    - passwords (list of strings)

    Returns an integer
    """

    quant_valid = 0
    for line in passwords:
        line = line.split()
        #Positions
        bounds = line[0].split('-')
        first_position = int(bounds[0]) - 1
        second_position = int(bounds[1]) - 1
        target = line[1][0]
        password = line[2]
        if password[first_position] == target and password[second_position] != target:
            quant_valid += 1
        elif password[first_position] != target and password[second_position] == target:
            quant_valid += 1
    return quant_valid
        
        
############################################
###                                      ###
###      Do not modify the code below    ###
###                EXCEPT                ###
###    to comment/uncomment the calls    ###
###        to the functions above        ###
###                                      ###
############################################

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"USAGE: python3 {os.path.basename(sys.argv[0])} <INPUT FILE>")
        sys.exit(1)

    input_file = sys.argv[1]

    if not os.path.exists(input_file):
        print(f"ERROR: No such file: {input_file}")
        sys.exit(1)

    with open(input_file) as f:
        passwords = [x for x in f.read().split()]

    print(f"Part 1:", part1(passwords))

    # Uncomment the following line when you're ready to work on Part 2
    #print(f"Part 2:", part2(passwords))
