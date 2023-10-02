def factorial(n) :
    # = n * factorial(n-1)
 if n < 0 :
    return "factorial is not define for negative numbers"
 elif  n == 0 or n == 1:
   return 1
 else:
   return n * factorial(n-1)
 
number = int(input("Enter a non-negative integer: "))
print(f"The factorial of {number} is {factorial(number)}")