"""*12. Remove Duplicates*  
Take a list with duplicates like `[1,2,2,3,4,4]` and return `[1,2,3,4]`."""
# making list
numbers = [56,87,45,87,23]
rev_numb = numbers[::-1]
lenth = len(numbers)
print(lenth)
for i in range(0, len(numbers)):
    if numbers[i] == numbers[i]:
               print(numbers[i])
               

"""
    for j in range(0, len(numbers)):
          if numbers[i] == rev_numb[j]:
               print("d")"""
print(numbers)
print(rev_numb)
"""
    for j in range(0, len(numbers)):
        if numbers[i] == numbers[j]:
            numbers.pop(i)
"""