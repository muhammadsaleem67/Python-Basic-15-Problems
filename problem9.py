"""*9. Prime Number Check*  
Check if a given number is prime. """
# take a input
number = int(input("Enter a number : "))
isPrime = True
if number == 1:
    isPrime = False # when it is one the prime is false
else :
    for i in range(2,number): 
        if number % i == 0 :
            isPrime = False
if isPrime:
    print("It is Prime Number")
else : print("It is not Prime Number")
