size = int(input("Enter the matrix size : "))

element = []
matrix = []

for i in range(size):
    for j in range(size):
        element.append(int(input()))
    matrix.append(element)
    element = []

    
l_rsum = 0
r_lsum = 0

for index in range(size):
    l_rsum += matrix[index][index]
print("Sum of left-to-right diagonal elements =", l_rsum)


for index in range(size):
    r_lsum += matrix[index][size - 1 - index]
print("Sum of right-to-left diagonal elements =", r_lsum)

print("\nAbsolute Difference =", abs(l_rsum - r_lsum))
