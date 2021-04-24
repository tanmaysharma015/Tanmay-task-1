matrix = []
interleaved_array = []

#input
no_of_arrays = int(input("Enter the number of arrays:"))     #this will act as rows
length = int(input("Enter the length of a single array:"))     #this will act as columns
print(" \n")

for i in range(no_of_arrays):          # A for loop for row entries
    a =[]
    print("enter the values of array " + str(i+1) + ": ")
    for j in range(length):      # A for loop for column entries
         a.append(int(input()))
    matrix.append(a)


#processing
for m in range(length):
    for n in range(no_of_arrays):
        interleaved_array.append(matrix[n][m])


#output
print(" \n\n\n\n")
print(interleaved_array)
