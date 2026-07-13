"""*13. Palindrome Check*  
Check if a word or phrase reads the same backwards. Ignore spaces and case.  
Example: `racecar` → True, `Hello` → False"""
# take input
word = input("Enter a word to check palingdrome : ")
rev_word = word[::-1]
if word == rev_word:
    print("the word is palingdrome")
else : 
    print("the word is not palingdrome")
