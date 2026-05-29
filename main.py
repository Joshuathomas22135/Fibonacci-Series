# Write a program to print the Fibonacci series up to n terms (given by the user).

terms = int(input("Enter the number of terms: "))

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
if terms <= 0:
    print("Please enter a positive number.")
else:
    print("Fibonacci Sequence:")
    for i in range(terms):
        print(fibonacci(i), end=" ")