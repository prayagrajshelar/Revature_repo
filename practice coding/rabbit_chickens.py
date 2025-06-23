# Write a program to solve a classic ancient Chinese puzzle: We count 35 heads and 94 legs among the chickens and rabbits in a farm. How many rabbits and how many chickens do we have?
# Hints
# Use for loop to iterate all possible solutions.


total_heads = 35
total_legs = 94

for chickens in range(total_heads + 1):
    rabbits = total_heads - chickens
    legs = 2 * chickens + 4 * rabbits
    if legs == total_legs:
        print("Chickens:", chickens)
        print("Rabbits:", rabbits)
        break
