
# n = int(input("Enter the number of odd number "))  
# # outer loop to handle number of odd  
# for i in range(0, n):  
#     # inner loop to handle number of columns  
#     # values is changing according to outer loop  
#         for j in range(0, i + 1):  
#             # printing stars  
#             print("* ", end="")       
  
#         # ending line after each row  
#         print()  
print("Program to print star pattern: \n");
rows = input("Enter maximum stars you want display on a single line")
rows = int (rows)
for i in range (0, num_rows):
    for j in range(0, i + 1):
        print("* ", end='')
    print("\r")
for i in range (num_rows, 0, -1):
    for j in range(0, i -1):
        print("* ", end='')
    print("\r")