"""3: Write a Python program to show flattening.
Tasks:
1. Take a 2D matrix.
2. Convert it into a ID vector.
3. Pass it to a fully connected layer.
4. Calculate final output manually.
5. Explain the role of flatten layer in CNN.
Input Matrix
matrix = [ [6, 4], [8, 6]
1
Expected Flatten Output
flatten_output [6, 4, 8, 6]
"""

# Program to demonstrate Flattening

# --------------------------------------------------
# 1. Input 2D Matrix
# --------------------------------------------------

matrix = [
    [6, 4],
    [8, 6]
]

print("Input Matrix:")

for row in matrix:
    print(row)


# --------------------------------------------------
# 2. Flatten the Matrix
# --------------------------------------------------

flatten_output = []

for row in matrix:
    for value in row:
        flatten_output.append(value)


print("\nFlatten Output:")
print(flatten_output)


# --------------------------------------------------
# 3. Fully Connected Layer
# --------------------------------------------------

# Weights for each input
weights = [0.2, 0.3, 0.4, 0.1]

# Bias
bias = 0.5


# --------------------------------------------------
# 4. Calculate Final Output Manually
# --------------------------------------------------

output = 0

for i in range(len(flatten_output)):

    multiplication = flatten_output[i] * weights[i]

    print(
        flatten_output[i],
        "*",
        weights[i],
        "=",
        multiplication
    )

    output = output + multiplication


# Add bias
output = output + bias


print("\nFinal Output:")
print(output)