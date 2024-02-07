# Number Distribution Algorithm

This Python script provides a solution to distribute a given list of numbers across a specified number of lines. The goal is to achieve a balanced distribution, where the sum of numbers in each line is as close to equal as possible.

## Author

- **Laís de Oliveira Dalle Mulle**
- **Email:** laisdallemulle@rrccompanies.com
## Date

- 2024-02-07

## Description

The algorithm employs a greedy approach to distribute numbers. It sorts the numbers in descending order and iteratively places each number in the line that, after the placement, would have the least total sum compared to the others. This method aims to minimize the difference between the sums of the lines, achieving a relatively balanced distribution without the need for exhaustive search.

## Usage

To use this script, you need to have Python installed on your system. You can then download or copy the script into a `.py` file and run it using a Python interpreter.

### Example

```python
# ==============================================================================
# Date: 2024-02-07
# Author: Laís de Oliveira Dalle Mulle
# Email: laisdallemulle@rrccompanies.com
# ==============================================================================

def distribute_numbers_greedy(numbers, num_lines):
    # Sorts the numbers to facilitate distribution starting with the largest
    numbers.sort(reverse=True)
    
    # Initializes lists to store the numbers in each line
    lines = [[] for _ in range(num_lines)]
    sums = [0] * num_lines
    
    # Distributes each number into the line that results in the least difference
    # in sums after the placement
    for number in numbers:
        # Finds the line with the least total sum
        idx = sums.index(min(sums))
        lines[idx].append(number)
        sums[idx] += number
    
    return lines, sums

# Example usage
numbers = [24, 24, 22, 24, 22, 22, 24, 22]  # List of numbers to be distributed
num_lines = 3  # Desired number of lines

lines_distributed, sums_lines = distribute_numbers_greedy(numbers, num_lines)

for i, line in enumerate(lines_distributed):
    print(f"Line {i+1}: {line} (Sum: {sums_lines[i]})")
