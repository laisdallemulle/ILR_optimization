# ==============================================================================
# Title: Distribution Algorithm
# Author: Laís de Oliveira Dalle Mulle
# Date: 2024-02-07
# Email: laisdallemulle@rrccompanies.com
#
# Description: This algorithm distributes a list of string qtys across a specified
# number of inverters in a greedy approach to achieve a balanced inverter load ratio (ILR).
# ==============================================================================


def distribute_numbers_greedy(numbers, num_lines):
    # Sorts the numbers to facilitate distribution starting with the largest
    numbers.sort(reverse=True)
    
    # Initializes lists to store the numbers in each line
    lines = [[] for _ in range(num_lines)]
    sums = [0] * num_lines
    
    # Distributes each number to the line that results in the smallest difference of sums after insertion
    for number in numbers:
        # Finds the line with the current smallest sum
        index_smallest_sum = sums.index(min(sums))
        lines[index_smallest_sum].append(number)
        sums[index_smallest_sum] += number
    
    return lines, sums

# Input values
numbers = [24, 24, 22, 24, 22, 22, 24, 22]  # List of numbers to be distributed
num_lines = 3  # Desired number of inverters
pot_inverter = 744.958
str_qty = 28
pot_module = 545.5 

distributed_lines, line_sums = distribute_numbers_greedy(numbers, num_lines)

# Prints the result
for i, line in enumerate(distributed_lines):
    print(f"Inverter {i+1}: {line} (~ILR: {((line_sums[i]*str_qty*(pot_module/1000))/pot_inverter)} )")
