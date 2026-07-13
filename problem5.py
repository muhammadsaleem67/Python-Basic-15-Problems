"""Take 3 numbers and print the largest without using `max()`."""
# taking three numbers
numb1 = 45
numb2 = 100
numb3 = 7
max = 0
if numb1 < numb2:
    max = numb2
elif numb2 < numb3:
    max = numb3
else :
    max = numb1
print(max)
# Complete