"""*10. Count Vowels & Consonants*  
Take a string and count how many vowels and consonants it has."""
# take input to check
vowels_or_consonent = input("Enter a word : ")
vcount = 0
ccount = 0
v = 0
c = 0
for i in range(0,len(vowels_or_consonent)):
    v = vowels_or_consonent[i]
    c = vowels_or_consonent[i]
    if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u' :
        vcount += 1
    elif c == 'b' or c == 'c' or c == 'd' or c == 'f' or c == 'g' or c == 'h' or c == 'j' or c == 'k' or c == 'l' or c == 'm' or c == 'n' or c == 'p' or c == 'q' or c == 'r' or c == 's' or c == 't' or c == 'v' or c == 'w' or c == 'x' or c == 'y' or c == 'z': 
        ccount += 1
    else : 
        print("Invalid Word")

for i in range(0, len(vowels_or_consonent)):
    if vowels_or_consonent[i] == 'b' or 'c' or 'd' or 'f' or 'g' or 'h' or 'j' or 'k' or 'l' or 'm' or 'n' or 'p' or 'q' or 'r' or 's' or 't' or 'v' or 'w' or 'x' or 'y' or 'z': 
        print(vowels_or_consonent[i])
print("Vowels / Consonents") 
print(vcount,"/",ccount)