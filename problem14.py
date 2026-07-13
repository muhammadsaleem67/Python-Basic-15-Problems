"""*14. Factorial Using Function*  
Write a function `factorial(n)` that returns n!. Test it with `factorial(5)`."""
# making function
def factorial(n):
    if n == 1:
        return 1
    else :
        print("factorial:",n)
        return n*factorial(n-1)
value = int(input("Enter any value:"))
print("Factorial of ",value,"is:",factorial(value))