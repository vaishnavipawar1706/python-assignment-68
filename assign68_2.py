"""2: Write a Python program to demonstrate ReLU and Max Pooling.
Tasks:
1. Create a feature map with positive and negative values.
2. Apply ReLU.
3. Apply 2x2 max pooling.
4. Display output after each step.
5. Explain why pooling reduces size.
Input Feature Map
feature_map = [
[3, 3, 3],
[0,0,0],
[-3, -3, -3]
ReLU Rule
If value < 0, convert it to 0
If value >= 0, keep it same

Expected Output
relu_output = [
    [3, 3, 3], 
    [0,0,0],
    [0,0,0]
]"""

# Program to demonstrate ReLU and Max Pooling

# --------------------------------------------------
# 1. Create Feature Map
# --------------------------------------------------

feature_map = [
    [3, 3, 3],
    [0, 0, 0],
    [-3, -3, -3]
]

print("Original Feature Map:")

for row in feature_map:
    print(row)


# --------------------------------------------------
# 2. Apply ReLU
# --------------------------------------------------

relu_output = []

for row in feature_map:

    new_row = []

    for value in row:

        if value < 0:
            new_row.append(0)
        else:
            new_row.append(value)

    relu_output.append(new_row)


print("\nAfter ReLU:")

for row in relu_output:
    print(row)


# --------------------------------------------------
# 3. Apply 2x2 Max Pooling
# --------------------------------------------------

pool_size = 2
stride = 2

pooled_output = []

rows = len(relu_output)
cols = len(relu_output[0])

for i in range(0, rows - pool_size + 1, stride):

    row = []

    for j in range(0, cols - pool_size + 1, stride):

        # Get 2x2 region
        region = [
            relu_output[i][j],
            relu_output[i][j + 1],
            relu_output[i + 1][j],
            relu_output[i + 1][j + 1]
        ]

        # Find maximum value
        maximum = max(region)

        row.append(maximum)

    pooled_output.append(row)


# --------------------------------------------------
# 4. Display Max Pooling Output
# --------------------------------------------------

print("\nAfter 2x2 Max Pooling:")

for row in pooled_output:
    print(row)


# --------------------------------------------------
# 5. Explanation
# --------------------------------------------------

print("Why does pooling reduce size?")
print("Max pooling takes a small region, such as 2x2,")
print("and replaces it with one maximum value.")
print("Therefore, the number of rows and columns decreases.")