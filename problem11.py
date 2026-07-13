"""Level 3: Lists, Strings & Functions
11. Find Max in List  
Create a list of 5 numbers and find the largest without using `max()`."""
numbers = [56,87,45,87,23]
max = 0
for i in range(0, len(numbers)):
    for j in range(0, len(numbers)):
        if numbers[i] > numbers[j]:
            max = numbers[i]
print(max)
