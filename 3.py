
# With a given integral number n, write a program to generate a dictionary that
# contains (i, i*i), an integral number between 1 and n (both included).
# Then, the program should print the dictionary. Suppose the following input is
# supplied to the program: 8 Then,
# the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

number = int(input("Enter the number: "))
dict= {}
for i in range(1, number + 1):
    number =  i**2
    dict[i] = number
print(dict)