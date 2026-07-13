"""7. Sum of First N Numbers  
Take `n` as input and print the sum of 1+2+3+...+n using a loop."""
# declare n as input
n = int(input("Enter a number : ")) +1
sum = 0
for i in range(1,n):
    sum = i + sum
print(sum)
