# Question
# You are given an integer, N. Your task is to print an alphabet rangoli of size N. (Rangoli is a form of Indian folk art based on creation of patterns.)
# Different sizes of alphabet rangoli are shown below:


# #size 3
# ----c----
# --c-b-c--
# c-b-a-b-c
# --c-b-c--
# ----c----
# #size 5
# --------e--------
# ------e-d-e------
# ----e-d-c-d-e----
# --e-d-c-b-c-d-e--
# e-d-c-b-a-b-c-d-e
# --e-d-c-b-c-d-e--
# ----e-d-c-d-e----
# ------e-d-e------
# --------e--------
 
# Hints
# First print the half of the Rangoli in the given way and save each line in a list. Then print the list in reverse order to get the rest.

import string

def print_rangoli(size):
    alpha = string.ascii_lowercase
    lines = []

    for i in range(size):
        left = '-'.join(alpha[size-1:i:-1])  # descending
        center = alpha[i]                    # middle character
        right = '-'.join(alpha[i+1:size])   # ascending
        full = (left + ('-' if left else '') + center + ('-' if right else '') + right).center(4*size-3, '-')
        lines.append(full)

    # Print top half + center + bottom half
    print('\n'.join(lines[::-1] + lines[1:]))

# Example usage:
print_rangoli(3)
print()
print_rangoli(5)
