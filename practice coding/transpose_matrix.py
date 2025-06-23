# Step 1: Input 2x2 matrix
matrix = []
print("Enter 4 elements for 2x2 matrix:")

for i in range(2):
    row = []
    for j in range(2):
        num = int(input(f"Element at [{i}][{j}]: "))
        row.append(num)
    matrix.append(row)

# Step 2: Transpose the matrix
transpose = [[0, 0], [0, 0]]
for i in range(2):
    for j in range(2):
        transpose[i][j] = matrix[j][i]

# Step 3: Print original and transposed matrices
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

print("\nTransposed Matrix:")
for row in transpose:
    print(row)

# Step 4: Compare both matrices
if matrix == transpose:
    print("\nOriginal and Transposed matrices are SAME.")
else:
    print("\nOriginal and Transposed matrices are DIFFERENT.")
