"""1: Write a Python program to manually perform convolution.
Input:
A 5x5 matrix representing grayscale image.
Kernel:
A 3x3 edge detection filter.
Tasks:
1. Move kernel over image.
2. Perform multiplication and addition.
3. Generate feature map.
4. Print each region calculation.
Input Image Matrix
image = [
[0, 0, 0, 0, 0],
[0, 0, 0, 0, 0],
[1, 1, 1, 1, 1],
[0,0,0,0,0],
[0, 0, 0, 0,01
Kernel Matrix
kernel = [
[-1, -1, -1],
[0,0,0],
[1, 1, 1]
First Region Calculation
Region:
000
000
111
Kernel:
-1-1-1
000
1 11
Calculation:

0*-1 0*-1 0*-1 +  

0 * 0 + 0 * 0 + 0 * 0+ 

1 * 1 + 1 * 1 + 1 * 1 

Output = 3

Expected Feature Map

feature_map = [

[3, 3, 3],

[0,0,0],

[-3, -3, -3]
"""

image = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]    
]

kernel = [
    [-1, -1, -1],
    [0,  0,  0],
    [1,  1,  1]   
]

feature_map = []

for i in range(3):
    row = []
    
    for j in range(3):
        region = [
            [image[i][j],     image[i][j+1],     image[i][j+2]],
            [image[i+1][j],   image[i+1][j+1],   image[i+1][j+2]],
            [image[i+2][j],   image[i+2][j+1],   image[i+2][j+2]]
        ]
        
        total = 0
        
        print("\nRegion:")
        for r in region:
            print(r)
            
        print("Kernal:")
        for k in kernel:
            print(k)
            
        print("Calculation:")
        
        for x in range(3):
            for y in range(3):
                multiplication = region[x][y] * kernel[x][y]

                print(
                    f"{region[x][y]} * {kernel[x][y]} = {multiplication}",
                    end="   "
                )

                total = total + multiplication

            print()

        print("Output =", total)

        row.append(total)

    feature_map.append(row)


# Print final feature map
print("Feature Map:")

for row in feature_map:
    print(row)